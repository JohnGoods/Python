#coding=utf-8
# import re

# test_str = "<div><p>岗位职责：</p><p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p><p><br></p><p>必备要求：</p><p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p><p>&nbsp;<br></p><p>技术要求：</p><p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p><p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p><p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p><p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p><p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p><p>&nbsp;<br></p><p>加分项：</p><p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p></div>"
#
# ret = re.sub(r"<[^>]*>|&nbsp;|\n", "\n", test_str)
# print(ret)

# str = '''
# Brand	LAGarden™
# Overall Size	48"Lx24"Wx60"H (4x2x5ft)
# Round Vent	2x 4" dia.
# 3x 6" dia.
# Rectangular Vent	2x(13-1/2"x4-1/2")
# 1x(21-3/4"x5")
# Overall Capacity	176 lbs(80Kg)
# Nylon Belts	4
# Exterior Material	210D
# Connector Material	Sturdy metal
# Frame	White paint coated metal rods
# Package Content	1x Reflective Growing Tent Cover
# 1set Metal Frame
# 1x Assembly Instruction
# 1x Removable Water-proof Mylar Floor tray as Free Gift
# '''
# #ret = re.sub(r"\n", " ", str)
# ret = re.sub(r"	", "----", str)
# print(ret)

#https://www.ebay.com/itm/382022359017

import re
_str = '''
<td width="172" bgcolor="#666666" style="padding:3px;";>Brand</td>
<td width="393" bgcolor="#CCCCCC" style="padding:3px; color:#000000;";>LAGarden™</td>
</tr>
<tr>
<td bgcolor="#666666"; style="padding:3px;">Overall Size</td>
<td bgcolor="#CCCCCC" style="padding:3px; color:#000000;";>48"Lx24"Wx60"H (4x2x5ft)</td>
</tr>
<tr>
<td bgcolor="#666666"; style="padding:3px;">Round Vent</td>
<td bgcolor="#CCCCCC" style="padding:3px; color:#000000;";>2x 4" dia.<br>
3x 6" dia.</td>
</tr>
<tr>
<td bgcolor="#666666"; style="padding:3px;">Rectangular Vent</td>
<td bgcolor="#CCCCCC" style="padding:3px; color:#000000;";>2x(13-1/2"x4-1/2")<br>1x(21-3/4"x5")</td>
</tr>
<tr>
<td bgcolor="#666666"; style="padding:3px;">Overall Capacity</td>
<td bgcolor="#CCCCCC" style="padding:3px; color:#000000;";>176 lbs(80Kg) </td>
</tr>
<tr>
<td bgcolor="#666666"; style="padding:3px;">Nylon Belts</td>
<td bgcolor="#CCCCCC" style="padding:3px; color:#000000;";>4</td>
</tr>
<tr>
<td bgcolor="#666666"; style="padding:3px;">Exterior Material</td>
<td bgcolor="#CCCCCC" style="padding:3px; color:#000000;";>210D</td>
</tr>
<tr>
<td bgcolor="#666666"; style="padding:3px;">Connector Material</td>
<td bgcolor="#CCCCCC" style="padding:3px; color:#000000;";>Sturdy metal</td>
</tr>
<tr>
<td bgcolor="#666666"; style="padding:3px;">Frame</td>
<td bgcolor="#CCCCCC" style="padding:3px; color:#000000;";>White paint coated metal rods</td>
</tr>
<tr>
<td rowspan="2" bgcolor="#666666"; style="padding:3px;">Package Content</td>
<td bgcolor="#CCCCCC" style="padding:3px; color:#000000;";>1x Reflective Growing Tent Cover
'''
ret = re.sub(r"<[^>]*>|&nbsp;|\n", ":", _str)
ret = re.sub(r":::", "\n", ret)
ret = re.sub(r":", "", ret)
print(ret)