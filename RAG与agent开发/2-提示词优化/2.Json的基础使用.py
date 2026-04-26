import json

d = {
    "name":"张三",
    "age":19 ,
    "gender":"男"
}
s1 = json.dumps(d,ensure_ascii=False)
print(s1)

n = [
    {
        "name":"张三",
        "age":19,
        "gender":"男"
    },
    {
        "name":"李四",
        "age":20,
        "gender":"男"
    },
    {
        "name":"王五",
        "age":19,
        "gender":"男"
    }
]

s2 = json.dumps(n,ensure_ascii=False)
print(s2)



json_str = '{"name": "张三", "age": 19, "gender": "男"}'
json_array_str = '[{"name": "张三", "age": 19, "gender": "男"}, {"name": "李四", "age": 20, "gender": "男"}, {"name": "王五", "age": 19, "gender": "男"}]'

res_dict = json.loads(json_str)
print(res_dict, type(res_dict))
res_list = json.loads(json_array_str)
print(res_list, type(res_list))