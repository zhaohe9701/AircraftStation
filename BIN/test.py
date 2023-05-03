import folium
from folium import MacroElement
from jinja2 import Template

# 创建一个Folium地图
m = folium.Map(location=[40.7128, -74.0060], zoom_start=10)

# 创建一个包含JavaScript函数的MacroElement对象
js_macro = MacroElement()
js_macro._template = Template(JS_FUNCTION.render())

# 将JavaScript函数绑定到地图加载完成事件上
m.get_root().add_child(js_macro)

# 将所有JavaScript和CSS嵌入到HTML文件中
m.save("map.html", embed=True)