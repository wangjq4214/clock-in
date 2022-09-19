login_url = "https://app.buaa.edu.cn/uc/wap/login/check"
info_url = "https://app.buaa.edu.cn/buaaxsncov/wap/default/get-info"
save_url = "https://app.buaa.edu.cn/buaaxsncov/wap/default/save"

# 失败重试次数
all_try_times = 3

# geo_api_info包含了在校园内已经获取的地理信息，就算不在学校也能用学校内的地理位置，相当于在学校内打卡
geo_api_info = {
    "type": "complete",
    "info": "SUCCESS",
    "status": 1,
    "dEa": "XX",
    "position": {
        "Q": 39.98493,
        "R": 116.34593999999998,
        "lng": 116.34594,
        "lat": 39.98493
    },
    "message": "Get ipLocation success.Get address success.",
    "location_type": "ip",
    "accuracy": None,
    "isConverted": True,
    "addressComponent": {
        "citycode": "010",
        "adcode": "110108",
        "businessAreas": [{
            "name": "五道口",
            "id": "110108",
            "location": {
                "Q": 39.99118,
                "R": 116.34157800000003,
                "lng": 116.341578,
                "lat": 39.99118
            }
        }],
        "neighborhoodType": "生活服务;生活服务场所;生活服务场所",
        "neighborhood": "北京航空航天大学",
        "building": "北京航空航天大学学生公寓13号楼",
        "buildingType": "商务住宅;住宅区;宿舍",
        "street": "北四环中路辅路",
        "streetNumber": "248号",
        "country": "中国",
        "province": "北京市",
        "city": "",
        "district": "海淀区",
        "township": "花园路街道"
    },
    "formattedAddress": "北京市海淀区花园路街道北京航空航天大学学生公寓13号楼北京航空航天大学学院路校区",
    "roads": [],
    "crosses": [],
    "pois": []
}
# 沙河校区的地理信息
'''
geo_api_info = {
    "type": "complete",
    "info": "SUCCESS",
    "status": 1,
    "dEa": "XX",
    "position": {
        "Q": 40.1546045,
        "R": 116.2735086,
        "lng": 116.2735086,
        "lat": 40.1546045
    },
    "message": "Get ipLocation success.Get address success.",
    "location_type": "ip",
    "accuracy": None,
    "isConverted": True,
    "addressComponent": {
        "citycode": "010",
        "adcode": "110114",
        "businessAreas": [{
            "name": "沙河",
            "id": "110114",
            "location": {
                "Q": 40.134237,
                "R": 116.280096,
                "lng": 116.280096,
                "lat": 40.134237
            }
        }],
        "neighborhoodType": "",
        "neighborhood": "",
        "building": "",
        "buildingType": "",
        "street": "南丰路",
        "streetNumber": "9号",
        "country": "中国",
        "province": "北京市",
        "city": "",
        "district": "昌平区",
        "township": "沙河镇"
    },
    "formattedAddress": "北京市昌平区沙河镇北京航空航天大学3号实验楼北京航空航天大学沙河校区",
    "roads": [],
    "crosses": [],
    "pois": []
}
'''
save_data_str = '''
sfzs: 1
bzxyy:
bzxyy_other:
brsfzc: 1
tw:
sfcxzz:
zdjg:
zdjg_other:
sfgl:
gldd:
gldd_other:
glyy:
glyy_other:
gl_start:
gl_end:
sfmqjc:
sfzc_14: 1
sfqw_14: 0
sfqw_14_remark:
sfzgfx: 0
sfzgfx_remark:
sfjc_14: 0
sfjc_14_remark:
sfjcqz_14: 0
sfjcqz_14_remark:
sfgtjz_14: 0
sfgtjz_14_remark:
szsqqz: 0
sfyqk:
szdd: 1
area: 
city: 
province: 
address: 
gwdz:
is_move: 0
move_reason:
move_remark:
realname: XX
number: XX
uid: XX
created: XX
date: XX
id: XX
gwszdd:
'''