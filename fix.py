import json

def fix_notebook_widgets(input_path, output_path=None):
    """
    Sửa lỗi:
    'state' key is missing from 'metadata.widgets'

    - Nếu metadata.widgets không có 'state' -> thêm state rỗng
    - Hoặc xóa luôn metadata.widgets nếu muốn sạch hoàn toàn
    """

    if output_path is None:
        output_path = input_path

    with open(input_path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    metadata = nb.get("metadata", {})

    # Kiểm tra widgets
    if "widgets" in metadata:
        widgets = metadata["widgets"]

        # Nếu thiếu state thì thêm
        if isinstance(widgets, dict) and "state" not in widgets:
            widgets["state"] = {}

        # Nếu muốn xóa hoàn toàn metadata.widgets thì bỏ comment dòng dưới
        del metadata["widgets"]

    nb["metadata"] = metadata

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

    print(f"Đã sửa notebook: {output_path}")
fix_notebook_widgets("aus-solar-generation-forecasting.ipynb")
fix_notebook_widgets("finetune_chronos.ipynb")