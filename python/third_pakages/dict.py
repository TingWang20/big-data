# 问题：dict 一行转换多行
# 待处理的数据
json_dict = {"code":'7200',"message":"success","result":
[
    {
    "thread_content":"真的不好，外形不好看，地盘也不好",
    "alg_ret":"外形_负面_不好看\n底盘_负面_底盘不好"
    }
]
}
# 处理的结果展示形式示范
json_dict = {"code":'7200',"message":"success","result":
[
    {
    "thread_content":"真的不好，外形不好看，地盘也不好",
    "alg_ret":[{"aspect":"外形","emotion":"负面","opinion":"不好看"}]
    },
    {
    "thread_content":"真的不好，外形不好看，地盘也不好",
    "alg_ret":[{"aspect":"底盘","emotion":"负面","opinion":"底盘不好"}]
    }
]
}
# 以下是代码展示
import json

json_dict = {
    "code": '7200',
    "message": "success",
    "result": [
        {
            "thread_content": "真的不好，外形不好看，地盘也不好",
            "alg_ret": "外形_负面_不好看\n底盘_负面_底盘不好"
        }
    ]
}

updated_dict = json_dict.copy()
results = updated_dict["result"]

for result in results:
    alg_ret = result["alg_ret"]
    alg_ret_list = alg_ret.split("\n")
    alg_ret_dicts = []

    for item in alg_ret_list:
        aspect, emotion, opinion = item.split("_")
        alg_ret_dict = {"aspect": aspect, "emotion": emotion, "opinion": opinion}
        alg_ret_dicts.append(alg_ret_dict)

    result["alg_ret"] = alg_ret_dicts

# 将更新后的 updated_dict 转换为 JSON 字符串，禁用 ASCII 编码
updated_json_str = json.dumps(updated_dict, ensure_ascii=False)

print(updated_json_str)
# show result
{
  "code": "7200",
  "message": "success",
  "result": [
    {
      "thread_content": "真的不好，外形不好看，地盘也不好",
      "alg_ret": [
        {
          "aspect": "外形",
          "emotion": "负面",
          "opinion": "不好看"
        },
        {
          "aspect": "底盘",
          "emotion": "负面",
          "opinion": "底盘不好"
        }
      ]
    }
  ]
}

