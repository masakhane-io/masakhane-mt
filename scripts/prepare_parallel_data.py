# scripts/prepare_parallel_data.py

src_lang = "sw"
tgt_lang = "en"

src_file = f"../jw300_utils/test/test.en-{src_lang}.{src_lang}"
tgt_file = f"../jw300_utils/test/test.en-{src_lang}.en"

out_src = f"train.{src_lang}"
out_tgt = f"train.{tgt_lang}"

with open(src_file, 'r', encoding='utf-8') as src_in, \
     open(tgt_file, 'r', encoding='utf-8') as tgt_in, \
     open(out_src, 'w', encoding='utf-8') as src_out, \
     open(out_tgt, 'w', encoding='utf-8') as tgt_out:
    
    for s_line, t_line in zip(src_in, tgt_in):
        if s_line.strip() and t_line.strip():
            src_out.write(s_line.strip() + "\n")
            tgt_out.write(t_line.strip() + "\n")

print("✅ Data written to:", out_src, "and", out_tgt)