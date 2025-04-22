import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source_lang", type=str, required=True)
    parser.add_argument("--target_lang", type=str, required=True)
    parser.add_argument("--output_dir", type=str, required=True)
    args = parser.parse_args()

    src_code = args.source_lang
    tgt_code = args.target_lang

    # ✅ Point to the test folder
    data_dir = os.path.join(os.path.dirname(__file__), "test")

    # Define the source and target paths
    src_path = os.path.join(data_dir, f"test.en-{src_code}.{src_code}")
    tgt_path = os.path.join(data_dir, f"test.en-{src_code}.{tgt_code}")

    # Output files for the preprocessed corpus
    out_src = os.path.join(args.output_dir, f"train.{src_code}")
    out_tgt = os.path.join(args.output_dir, f"train.{tgt_code}")

    # Create the output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)

    with open(src_path, 'r', encoding='utf-8') as src_in, \
         open(tgt_path, 'r', encoding='utf-8') as tgt_in, \
         open(out_src, 'w', encoding='utf-8') as src_out, \
         open(out_tgt, 'w', encoding='utf-8') as tgt_out:

        for s_line, t_line in zip(src_in, tgt_in):
            s_line = s_line.strip()
            t_line = t_line.strip()
            if s_line and t_line:
                # Write lines to output files if both are non-empty
                src_out.write(s_line + "\n")
                tgt_out.write(t_line + "\n")

    print(f"✅ Saved preprocessed corpus to: {out_src} and {out_tgt}")

if __name__ == "__main__":
    main()