import xml.etree.ElementTree as et
t = et.parse('./HY202103_D07_(0,0)_LION1_DCM_LMZC.xml')
r = t.getroot()

#xml 태그 구성
#print(root.tag)
#for child in root:
#    print(child.attrib)

#태그 조건으로 검색하기
user = t.find('.//IVMeasurement[1]/Voltage').text
print(user)
use = t.find('.//IVMeasurement[1]/Current').text
print(use)

#태그 여러 개 한꺼번에 가져오기
for ElectroOpticalMeasurements in r.findall('ElectroOpticalMeasurements'):
    Voltage = ElectroOpticalMeasurements.find('.//IVMeasurement/Voltage').text
    Current = ElectroOpticalMeasurements.find('.//IVMeasurement/Current').text
print('Voltage:', Voltage)
print('Current:', Current)