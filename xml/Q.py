import xml.etree.ElementTree as et
t = et.parse('./HY202103_D07_(0,0)_LION1_DCM_LMZC.xml')
r = t.getroot()

#v,i 가져오기
v = t.find('.//IVMeasurement[1]/Voltage').text
i = t.find('.//IVMeasurement[1]/Current').text

#리스트화
vl = [float(a.strip()) for a in v.split(',')] # strip()은 공백 문자, 탭, 개행 등을 제거
il = [float(a.strip()) for a in i.split(',')] # 실수

print('Voltage:', vl)
print('Current:', il)