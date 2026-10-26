"""Apply the Issue #2 style-category display layer without changing raw catalog data."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
def configuration():
    config=json.loads((ROOT/'docs/style-categories.json').read_text(encoding='utf-8'))
    assert len(config['categories'])==8 and len(config['assignments'])==314
    assert set(config['assignments'].values())=={c['id'] for c in config['categories']}
    return config
def patch_html(raw, config=None):
    config=configuration() if config is None else config
    text=raw.decode('utf-8').replace('\r\n','\n')
    assert 'style-category-index' not in text
    assert '</head>' in text
    return text.replace('</head>','<script type="application/json" id="style-category-index">'+json.dumps(config,ensure_ascii=False,separators=(',',':'))+'</script></head>',1).encode('utf-8')
def patch_js(raw):
    js=raw.decode('utf-8').replace('\r\n','\n')
    assert 'const styleCategoryIndex=' not in js
    anchor = "  const preferencesKey=demoMode?'moss_image_demo_preferences':'moss_image_review_preferences';"
    extra = '\n  // Independent classification: raw catalog records, images and prompts stay intact.\n  const styleCategoryIndex=JSON.parse($(\'style-category-index\')?.textContent||\'{"categories":[],"assignments":{}}\');\n  const styleCategories=new Map(styleCategoryIndex.categories.map(category=>[category.id,category]));\n  const styleCategoryLabels=new Map(styleCategoryIndex.categories.map(category=>[category.en,category]));\n  function assignedStyleCategory(record){return styleCategories.get(styleCategoryIndex.assignments[record.key]);}\n'
    assert anchor in js
    js = js.replace(anchor, anchor + extra, 1)
    anchor = '    record.copyright=canonical;'
    assert anchor in js
    anchor2 = '    return {raw,stamp,record,displayVersion:'
    assert anchor2 in js
    js = js.replace(anchor2, "    const styleCategory=record.kind==='style'?assignedStyleCategory(record):null;\n    if(styleCategory){record.copyright=styleCategory.en;record.copyright_en=styleCategory.en;record.facets.copyright=[styleCategory.en];}\n" + anchor2, 1)
    anchor3 = "+' '+(record.anima_trigger||'')).toLowerCase()"
    assert anchor3 in js
    js = js.replace(anchor3, "+' '+(record.anima_trigger||'')+' '+(styleCategory?styleCategory.en+' '+styleCategory.ja:'')).toLowerCase()", 1)
    js = js.replace("function activeDimensions(){return catalogView==='style'?['character','copyright']:dimensions;}", "function activeDimensions(){return catalogView==='style'?['copyright','character']:dimensions;}", 1)
    js = js.replace('function facetValueLabel(key,value){', "function facetValueLabel(key,value){if(catalogView==='style'&&key==='copyright'&&styleCategoryLabels.has(value))return styleCategoryLabels.get(value)[language];", 1)
    js = js.replace('function copyrightDisplay(record){', "function copyrightDisplay(record){if(record.kind==='style'&&styleCategoryLabels.has(record.copyright))return styleCategoryLabels.get(record.copyright)[language];", 1)
    anchor4 = "    $('favorites-only').checked=!!prefs.favoritesOnly;showHidden=!!prefs.showHidden;hiddenOnly=!!prefs.hiddenOnly;"
    assert anchor4 in js
    js = js.replace(anchor4, "    if(catalogView==='style'&&styleCategoryIndex.categories.length)filters.copyright.delete('Picture styles');\n" + anchor4, 1)
    return js.encode("utf-8")
