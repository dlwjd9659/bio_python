import sys
import json

def read_csv(file_name: str) -> list:
    ret = []
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith('s'):
                header = line.strip().split(',')
                continue
            splitted = line.strip().split(',')
            d = dict(zip(header, splitted))
            ret.append(d)
    return ret

def w_json(list, file_name: str) -> None:
    with open(file_name, 'w') as handle:
        json.dump(list, handle, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("#usage: python {sys.argv[0]} [csv]")
        sys.exit()


    file_name = sys.argv[1]
    ret = read_csv(file_name)
    w_json(ret, "result_ass.json")
