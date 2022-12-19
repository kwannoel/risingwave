import re


def main():
    logfilepath = "/Users/noelkwan/projects/risingwave/debug/frontend-4566.log"
    with open(logfilepath, "r") as logs:
        is_semi = False
        sort_agg = False
        order_by = False
        for line in logs.readlines():
            if skip:
                skip -= 1
                continue
            line = line.strip()
            if "Left semi received: Ok(DataChunk { cardinality = " in line:
                line = line.strip("Left semi received: Ok(DataChunk { cardinality = ")
                # print(line)
                grps = re.match("^([0-9]*), capacity = ([0-9]*),", line)
                if grps is None:
                    continue
                (cardinality, _cap) = grps.groups()
                print(cardinality)
                skip = 1 # skip header
                is_semi = true
            if is_semi:
                (v1, v2, v3, v4) =\
                    re.match("^| (\d+) | (\d+) | (\d+) | (\d+) | (2022-01-01 00:00:00) |")


if __name__ == "__main__":
    main()
