import yaml


def get_calculate_data(path="test_data/calculate.yaml"):
    list_result = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = yaml.safe_load(stream=f.read())
        for x in content.values():
            for y in x:
                list_result.append((y.get("oper"), y.get("a"), y.get("b"),y.get("expect"), y.get("desc")))
        return list_result
    except FileNotFoundError:
        print("路径不正确")


if __name__ == '__main__':
    print(get_calculate_data(path="calculate.yaml"))
