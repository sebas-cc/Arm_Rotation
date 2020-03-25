# Copyright [2020] [Sebastian Camacho]

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

 #      http://www.apache.org/licenses/LICENSE-2.0

 #  Unless required by applicable law or agreed to in writing, software
 #  distributed under the License is distributed on an "AS IS" BASIS,
 #  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 #  See the License for the specific language governing permissions and
 #  limitations under the License.
   
comando=""
vd=0
vi=0
while comando!="s":
	c=0
	comando=input("left(l), right(r) or stop(s)?: ")
	m=int(input("cuanto lo va a mover?: "))
	if comando=="r":
		p=0
		while c<m:
			p+=1
			c+=1
			if p>359:
				p=0
				vd+=1
	elif comando=="l":
		p=359
		while c>-m:
			p-=1
			c-=1
			if p<0:
				p=359
				vi+=1
	print(f"Last position: {p}")
v=vi+vd
print(f"left: {vi}\nright: {vd}\nTotal laps: {v}")
