"use strict";
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const source=fs.readFileSync(path.join(__dirname,'../demo/review.js'),'utf8');
const helper=source.match(/  function resetRouteSearch\(\)\{[^\n]+/)[0];
const first=source.indexOf('if(first){const run=');
assert.ok(first>=0);
const navigation=source.slice(first+'if(first){'.length,source.indexOf('const focus=',first));
let checks=0;
for(const route of ['?tab=styles','?tab=creatures','?category=chinese-animation','?category=kyoto-animation','?run=fixture-run']){
 const ui={search:{value:'pikachu'},run:{value:''},'favorites-only':{checked:true}};
 const filters={character:new Set(['pikachu']),copyright:new Set(['Pokemon'])};
 const ctx={URLSearchParams,location:{search:route},restoredRoute:'',requestedTab:new URLSearchParams(route).get('tab'),requestedRun:new URLSearchParams(route).get('run'),data:{runs:[{id:'fixture-run',kind:'style'}],entries:[]},dimensions:Object.keys(filters),filters,$:key=>ui[key],resetMainSearch:()=>{ui.search.value='';},page:3,restoredScrollY:320,catalogView:'character',showHidden:true,hiddenOnly:true,isCreature:()=>false,localize(){},chineseAnimationGroup:'Chinese Animation',kyotoAnimationGroup:'Kyoto Animation'};
 vm.runInNewContext(helper+'\n'+navigation,ctx);
 assert.equal(ui.search.value,'',route);assert.equal(ctx.page,1);assert.equal(ctx.restoredScrollY,0);checks++;
}
{
 const ui={search:{value:'ink'},run:{value:''},'favorites-only':{checked:false}};
 const ctx={location:{search:'?tab=styles'},restoredRoute:'?tab=styles',requestedTab:'styles',requestedRun:null,data:{runs:[]},$:key=>ui[key],resetMainSearch:()=>{throw Error('same-route reload must retain search');},page:3,restoredScrollY:320,localize(){}};
 vm.runInNewContext(helper+'\n'+navigation,ctx);assert.equal(ui.search.value,'ink');assert.equal(ctx.page,3);assert.equal(ctx.restoredScrollY,320);checks++;
}
const drawing=source.slice(source.indexOf('  function drawTrialFacetWindow('),source.indexOf('  function populateTrialFacet('));
class Node{
 constructor(){this.children=[];this.style={};this.classList={toggle(){}};this.clientHeight=150;this.top=0;}
 get scrollHeight(){return this.children.reduce((sum,node)=>sum+(parseFloat(node.style.height)||32),0);}
 set scrollTop(value){this.top=Math.max(0,Math.min(value,Math.max(0,this.scrollHeight-this.clientHeight)));}
 get scrollTop(){return this.top;}
 setAttribute(){} contains(){return false;} replaceChildren(){this.children=[];this.top=0;} append(node){this.children.push(node);}
}
for(const [total,saved] of [[24,320],[200,320],[200,1e9],[3,1e9]]){
 const list=new Node(),state={key:'character',details:{open:true},list,visibleChoices:Array.from({length:total},(_,i)=>['item'+i,1]),scrollTop:saved};
 const ctx={facetExperiment:true,catalogView:'character',heights:{},document:{activeElement:null,createElement:()=>new Node()},trialFacetRow:()=>new Node(),t:key=>key};
 vm.runInNewContext(drawing,ctx);ctx.drawTrialFacetWindow(state,true);
 const expected=Math.min(saved,Math.max(0,total*32-150));
 assert.equal(list.scrollTop,expected);assert.equal(state.scrollTop,expected);checks++;
}
console.log(JSON.stringify({passed:true,checks,scope:'actual navigation and facet-render functions; modeled DOM clamping'}));
