"use strict";
const assert=require("node:assert/strict"),fs=require("node:fs"),path=require("node:path"),http=require("node:http");
const {chromium}=require("playwright");
const work=path.resolve(__dirname,".."),baseline=process.argv.includes("--baseline");
const roots={public:path.join(work,'demo')};
const sample=JSON.parse(fs.readFileSync(path.join(work,"demo/catalog.json"),"utf8"));
const large={...sample,entries:[...Array.from({length:200},(_,i)=>{const name=`Fixture character ${String(i).padStart(3,"0")}`;return{...sample.entries[0],key:`fixture:${i}`,id:`fixture-${i}`,name,name_jp:"",name_cn:"",copyright:"Fixture Work",facets:{...sample.entries[0].facets,character:[name],copyright:["Fixture Work"]},copy_tags:name};}),...sample.entries.filter(r=>r.kind==="style")]};
const pixel=Buffer.from("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQIHWP4z8DwHwAFgAI/ScLbtAAAAABJRU5ErkJggg==","base64");
let mutations=0;
const server=http.createServer((req,res)=>{
 const url=new URL(req.url,"http://127.0.0.1"),referer=new URL(req.headers.referer||"http://127.0.0.1");
 if(req.method!=="GET"){mutations++;res.writeHead(403).end("Test server is read-only");return;}
 if(url.pathname==="/blank"){res.writeHead(200,{"Content-Type":"text/html"}).end("<!doctype html><title>Isolated fixture</title>");return;}
 if(url.pathname==="/api/list"||url.pathname.endsWith("/catalog.json")){
  const data=referer.searchParams.get("fixture")==="large"?large:sample;
  res.writeHead(200,{"Content-Type":"application/json"}).end(JSON.stringify({...data,token:"isolated-fixture",folder_available:true}));return;
 }
 if(url.pathname==="/image"||/\/images\/\d+\.webp$/.test(url.pathname)){res.writeHead(200,{"Content-Type":"image/png"}).end(pixel);return;}
 const [variant,...parts]=url.pathname.slice(1).split("/");
 if(!roots[variant]){res.writeHead(404).end();return;}
 const file=path.resolve(roots[variant],parts.join("/")||"index.html");
 if(!file.startsWith(path.resolve(roots[variant])+path.sep)||!fs.existsSync(file)){res.writeHead(404).end();return;}
 let bytes=fs.readFileSync(file);
 if(file.endsWith("review.js")&&referer.searchParams.get("normal")==="1")bytes=Buffer.from(bytes.toString("utf8").replace("const facetExperiment=true;","const facetExperiment=false;"));
 res.writeHead(200,{"Content-Type":file.endsWith(".js")?"text/javascript":file.endsWith(".css")?"text/css":"text/html","Cache-Control":"no-store"}).end(bytes);
});
(async()=>{
 fs.mkdirSync(path.join(work,"artifacts"),{recursive:true});
 await new Promise(resolve=>server.listen(0,"127.0.0.1",resolve));
 const base=`http://127.0.0.1:${server.address().port}`;let browser;const results=[];
 console.log(`Read-only fixture service: pid=${process.pid}, port=${server.address().port}, command=node tests/browser.cjs${baseline?" --baseline":""}`);
 try{
  browser=await chromium.launch({headless:true,...(process.env.SBE_CHROMIUM_EXECUTABLE?{executablePath:process.env.SBE_CHROMIUM_EXECUTABLE}:process.platform==='win32'?{channel:'chrome'}:{})});
  for(const variant of Object.keys(roots)){
   const context=await browser.newContext({viewport:{width:1500,height:1000}}),page=await context.newPage(),errors=[];
   page.on("pageerror",error=>errors.push(error.message));
   const url=`${base}/${variant}/index.html`,ready=()=>page.waitForFunction(()=>document.querySelectorAll("#grid .card").length>0||document.querySelector("#empty")?.hidden===false);
   const fresh=async suffix=>{await page.goto(base+"/blank");await page.evaluate(()=>localStorage.clear());await page.goto(url+(suffix||""));await ready();};
   const check=(name,actual,expected)=>{const passed=JSON.stringify(actual)===JSON.stringify(expected);results.push({variant,name,actual,expected,passed});if(!baseline)assert.equal(passed,true,JSON.stringify(results.at(-1)));};
   await fresh("");await page.locator("#search").fill("pikachu");await page.locator("#search").press("Enter");
   await page.waitForFunction(()=>document.querySelectorAll("#grid .card").length===1);
   if(variant==="public")await page.locator('a[href="?tab=styles"]').click();else await page.goto(url+"?tab=styles");
   await page.waitForFunction(()=>document.querySelector("#tab-styles").getAttribute("aria-pressed")==="true");
   check("style URL clears character search",await page.locator("#search").inputValue(),"");
   check("style URL displays all 24 styles",await page.locator("#grid .card").count(),24);
   for(const mode of ["small","large",...(baseline?[]:["normal"])]){
    await fresh(mode==="large"?"?fixture=large":mode==="normal"?"?normal=1":"");
    const details=page.locator('details[data-facet="character"]');await details.locator("summary").click();
    const list=details.locator(".facet-list");await list.waitFor();
    const before=await list.evaluate(node=>{node.scrollTop=320;node.dispatchEvent(new Event("scroll"));return node.scrollTop;});
    assert.equal(before,320,JSON.stringify({variant,mode,metrics:await list.evaluate(node=>({children:node.children.length,height:node.clientHeight,scrollHeight:node.scrollHeight,text:node.textContent.slice(0,150)}))}));
    await page.reload();await ready();await list.waitFor();
    check(`${mode} facet restores scroll after reload`,await list.evaluate(node=>node.scrollTop),before);
    if(baseline)continue;
    // Force a rerender while the facet is closed, then reopen it.
    const opened=expected=>page.waitForFunction(expected=>JSON.parse(localStorage.getItem(document.documentElement.dataset.catalogMode==='demo'?'moss_image_demo_preferences':'moss_image_review_preferences')||'{}').opened?.character===expected,expected);
    await details.locator("summary").click();await opened(false);
    await page.locator("#language").selectOption("ja");
    await details.locator("summary").click();await opened(true);
    check(`${mode} closed facet preserves scroll`,await list.evaluate(node=>node.scrollTop),320);
    await page.locator("#language").selectOption("en");
    check(`${mode} language change preserves scroll`,await list.evaluate(node=>node.scrollTop),320);
    await list.evaluate(node=>{node.style.height="300px";});
    check(`${mode} resized facet preserves scroll`,await list.evaluate(node=>node.scrollTop),320);
    await list.evaluate(node=>{node.scrollTop=999999;node.dispatchEvent(new Event("scroll"));});
    const maximum=await list.evaluate(node=>node.scrollTop);await page.reload();await ready();await list.waitFor();
    check(`${mode} maximum saved position is clamped`,await list.evaluate(node=>node.scrollTop),maximum);
    const route=page.url();await page.goto(base+"/blank");
    await page.evaluate(()=>{
      const key=document.documentElement.dataset.catalogMode==='demo'?'moss_image_demo_preferences':'moss_image_review_preferences';
      // The blank document has no demo attribute, so update whichever preference
      // object the previous fixture page actually created.
      const stored=localStorage.getItem('moss_image_demo_preferences')?'moss_image_demo_preferences':key;
      const prefs=JSON.parse(localStorage.getItem(stored));prefs.facetScrolls.character=1e9;localStorage.setItem(stored,JSON.stringify(prefs));
    });
    await page.goto(route);await ready();await list.waitFor();
    const clamped=await list.evaluate(node=>({value:node.scrollTop,max:node.scrollHeight-node.clientHeight}));
    check(`${mode} obsolete oversized saved offset is clamped`,clamped.value,clamped.max);
   }
   if(!baseline){
    await fresh("?tab=styles");check("direct style URL",await page.locator("#grid .card").count(),24);
    const style=sample.entries.find(item=>item.kind==="style").name;
    await page.locator("#search").fill(style);await page.locator("#search").press("Enter");await page.reload();await ready();
    check("same style URL reload preserves search",await page.locator("#search").inputValue(),style);
    check("same style URL reload retains style tab",await page.locator("#tab-styles").getAttribute("aria-pressed"),"true");
    await fresh("");await page.locator("#search").fill("pikachu");await page.locator("#search").press("Enter");
    await page.locator("#tab-styles").click();await page.locator("#search").fill(style);await page.locator("#search").press("Enter");
    await page.locator("#tab-characters").click();check("character tab keeps its own search",await page.locator("#search").inputValue(),"pikachu");
    await page.locator("#tab-styles").click();check("style tab keeps its own search",await page.locator("#search").inputValue(),style);
    for(const target of ["?tab=creatures","?category=chinese-animation","?category=kyoto-animation"]){
     await fresh("");await page.locator("#search").fill("pikachu");await page.locator("#search").press("Enter");await page.goto(url+target);
     await page.waitForFunction(()=>document.querySelector("#connection").textContent!=="読み込み中…");
     check(`${target} clears previous search`,await page.locator("#search").inputValue(),"");
    }
    await fresh("");await page.locator("#page-size").selectOption("12");await page.locator('[data-page-step="1"]').first().click();
    await page.goto(url+"?tab=styles");await ready();
    check("different route resets page",await page.locator("[data-page-input]").first().inputValue(),"1");
    await page.screenshot({path:path.join(work,`artifacts/${variant}-verified.png`)});
    assert.deepEqual(errors,[],`${variant}: JavaScript errors`);
   }
   await context.close();
  }
  assert.equal(mutations,0,"No catalog write endpoint may be called");
  const report={baseline,checks:results.length,failed:results.filter(row=>!row.passed).length,mutations,results};
  fs.writeFileSync(path.join(work,`artifacts/${baseline?"baseline":"browser"}-results.json`),JSON.stringify(report,null,2));
  console.log(JSON.stringify({baseline,checks:report.checks,failed:report.failed,mutations}));
 }finally{
  await browser?.close();await new Promise(resolve=>server.close(resolve));await assert.rejects(fetch(base));console.log("Fixture service stopped; listener closed and HTTP unavailable");
 }
})().catch(error=>{console.error(error);process.exitCode=1;});
