files = [
    "short_S1.txt",
    "short_S2.txt",
    "short_S3.txt",
    "short_S4.txt",
    "short_S5.txt",
    "short_S6.txt",
    "short_S7.txt",
    "short_S8.txt",
    "short_S9.txt"
    ]

combo_fp = "all_results.csv"
combo_header = ["Run", "Task", "Operation", "Time", "Unit", "Percentage", "Run type"]
with open(combo_fp, "w") as f: 
    f.write(",".join(combo_header))
    f.write("\n")


header = [["Task", "Operation", "Time", "Unit"]]
for fp in files: 
    lines = [] 
    out_fp = fp.split(".")[0] + ".csv"
    with open(fp, "r") as f: 
        for line in f: 
            terms = line.split("|")
            line_list = []
            for term in terms: 
                if len(term.strip()) > 0:
                    line_list.append(term.strip())
            lines.append(line_list) 
    with open(out_fp, "w") as f: 
        for line in header + lines: 
            f.write(",".join(line))
            f.write("\n")
    with open(combo_fp, "a+") as f: 
        for line in lines: 
            aug_line = [fp.split(".")[0]] + line
            for i in range(len(aug_line)): 
                if aug_line[i].startswith("expensive"): 
                    aug_line[i] = "_".join(aug_line[i].split("-")[1:])
            # also add in percentage and which branch it is, based on run name (first entry in aug_line)
            percentage = aug_line[0].split("_")[-1]
            run_type = "_".join(aug_line[0].split("_")[:-1])
            aug_line.append(percentage)
            aug_line.append(run_type)
            f.write(",".join(aug_line))
            f.write("\n")
