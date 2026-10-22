const fs=require('fs'),vm=require('vm'),assert=require('assert');
const source=fs.readFileSync(__dirname+'/../demo/review.js','utf8');
const body=source.slice(source.indexOf('  function compareRecords('),source.indexOf('  function facetCounts('));
let rows=[],order='copyright';
const items=new Map();
const ctx={catalogCollator:new Intl.Collator('en',{numeric:true}),ensureCatalog:()=>({items}),$ :()=>({value:order}),copyrightCountKey:r=>r.copyright,smallCopyrightGroup:'Other',copyrightTotals:()=>{const m=new Map();for(const r of rows)m.set(r.copyright,(m.get(r.copyright)||0)+1);return m;}};
vm.createContext(ctx);vm.runInContext(body,ctx);
function sort(input,by='copyright') { rows=input;order=by;items.clear();for(const r of rows)items.set(r.key,{copyrightSort:r.copyright,renderedSort:r.time||0});return [...rows].sort(ctx.compareRecords); }
const character=(key,count,copyright='Pokemon')=>({key,name:key,source_count:count,kind:'character',copyright});
assert.deepEqual(sort([character('a',1),character('z',100),character('missing',undefined),character('zero',0)]).map(r=>r.key),['z','a','zero','missing']);
assert.equal(sort([character('a',1),character('z',100)],'name')[0].key,'a');
assert.equal(sort([{...character('a',1),time:10},{...character('z',100),time:20}],'oldest')[0].key,'a');
assert.equal(sort([{...character('a',1),time:10},{...character('z',100),time:20}],'newest')[0].key,'z');
const grouped=sort([character('small',999999,'One'),character('a',1),character('z',100),character('other',999999,'Other')]);
assert.deepEqual(grouped.map(r=>r.key),['z','a','small','other']);
assert.equal(sort([{...character('z',100),kind:'style'},{...character('a',1),kind:'style'}])[0].key,'a');
const samples=JSON.parse(fs.readFileSync(__dirname+'/../demo/catalog.json','utf8')).entries.filter(r=>r.kind==='character');
for(const work of new Set(samples.map(r=>r.copyright))){const result=sort(samples.filter(r=>r.copyright===work));for(let i=1;i<result.length;i++)assert(result[i-1].source_count>=result[i].source_count);}
console.log(JSON.stringify({passed:true,characters:samples.length,unknownCountsLast:true,preserved:['work grouping','Other last','name','oldest','newest','style ordering']}));
