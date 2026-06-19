import json
import io
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

SKILL_NAME = "jra-van-spec-skills"
DESC = ("JRA-VAN Data Lab. の JV-Data 仕様と JV-Link COM API の参照ガイド。"
        "レコードフォーマット/コード表/メソッド/戻り値コード/dataspec/option/"
        "C#構造体・固定長Shift_JISパースを references/spec/ から正確に答える。")

EVALS = [
    # --- should trigger (JV-Data / JV-Link spec, C# parsing, dataspec, codes) ---
    {"id": 1,  "query": "SEレコード（馬毎レース情報）の確定着順って先頭から何バイト目？あと入線順位と確定着順って別項目だっけ。固定長のオフセット教えて", "should_trigger": True},
    {"id": 2,  "query": "当日のリアルタイムオッズをJVRTOpenで取りたい。馬単と3連単は要らないんだけど、その場合dataspecは0B31〜0B33と0B35だけ指定すればいい？", "should_trigger": True},
    {"id": 3,  "query": "JV-LinkのJVOpen呼んだら戻り値-202が返ってきた。前のセッション閉じ忘れ？原因と対処を知りたい", "should_trigger": True},
    {"id": 4,  "query": "C#で馬連オッズ(O2)の構造体をパースしたい。Shift_JISの固定長で、オッズが繰り返し項目になってると思うんだけど読み出し位置の計算どうやる", "should_trigger": True},
    {"id": 5,  "query": "金曜の夜に翌日土曜のレースを先読みしたい。JVOpenのoptionは2(今週)でRA/SE取ればいい？fromtimeはどう指定する", "should_trigger": True},
    {"id": 6,  "query": "開催中に天候が晴→雨に変わったのを時系列で記録したい。WEレコードと変更識別の使い方教えて", "should_trigger": True},
    {"id": 7,  "query": "払戻レコード(HR)に3連単の払戻って何通りまで入る？同着のときの構造も知りたい", "should_trigger": True},
    {"id": 8,  "query": "トラックコードで芝の内回りと外回りってどう区別するの？コード値の一覧ほしい。あと競馬場コードも", "should_trigger": True},
    {"id": 9,  "query": "keibalensのインポート処理でRAレコード取り込んでるんだけど、グレードコードの値(A/B/C..)が何のグレードか分からん。コード表ある？", "should_trigger": True},
    {"id": 10, "query": "JV-Linkでイベント監視して、レース確定したら自動で結果データ取りに行きたい。JVWatchEventからJVRTOpenまでの実装の流れを知りたい", "should_trigger": True},

    # --- should NOT trigger (near-misses: shares 競馬/オッズ/C#/Shift_JIS/レジストリ/netkeiba) ---
    {"id": 11, "query": "今週末の宝塚記念、軸はどの馬がいいと思う？人気馬で堅そうなの教えて", "should_trigger": False},
    {"id": 12, "query": "馬連と3連複、回収率を上げるならどっちに比重置くべき？資金配分の考え方を教えて", "should_trigger": False},
    {"id": 13, "query": "netkeibaの出馬表ページをPythonのrequestsとBeautifulSoupでスクレイピングするコード書いて", "should_trigger": False},
    {"id": 14, "query": "LightGBMで競走馬の着順予測モデル作りたい。特徴量エンジニアリングのアイデアちょうだい", "should_trigger": False},
    {"id": 15, "query": "C#でCSVファイルを読み込んでDataTableに変換する汎用メソッド書いて。区切りはカンマ", "should_trigger": False},
    {"id": 16, "query": "Shift_JISで保存された古いテキストファイルがUTF-8環境で文字化けする。直す一般的な方法は？", "should_trigger": False},
    {"id": 17, "query": "Windowsのレジストリにアプリの設定を保存・読み込みするC#のサンプルちょうだい", "should_trigger": False},
    {"id": 18, "query": "サンデーサイレンス系で活躍した種牡馬を年代別に教えて。血統の話がしたい", "should_trigger": False},
    {"id": 19, "query": "次のG1っていつ？有馬記念の日程と発走時刻が知りたいだけ", "should_trigger": False},
    {"id": 20, "query": "SQLiteでレース結果テーブルを正規化したい。馬・レース・着順をどう分ければいい？主キー設計の相談", "should_trigger": False},
]

base = Path(__file__).resolve().parent  # eval/ ディレクトリ（このスクリプトと同じ場所）
tpl_path = Path(r"C:\Users\moroz\.copilot\installed-plugins\anthropic-agent-skills\example-skills\skills\skill-creator\assets\eval_review.html")

# write evals.json (skill-creator schema: array of {query, should_trigger})
evals_simple = [{"query": e["query"], "should_trigger": e["should_trigger"]} for e in EVALS]
(base / "evals").mkdir(parents=True, exist_ok=True)
(base / "evals" / "trigger_eval.json").write_text(json.dumps(evals_simple, ensure_ascii=False, indent=2), encoding="utf-8")

# fill template
html = tpl_path.read_text(encoding="utf-8")
html = html.replace("__SKILL_NAME_PLACEHOLDER__", SKILL_NAME)
html = html.replace("__SKILL_DESCRIPTION_PLACEHOLDER__", DESC)
html = html.replace("__EVAL_DATA_PLACEHOLDER__", json.dumps(evals_simple, ensure_ascii=False))
out = base / "eval_review_jra-van-spec-skills.html"
out.write_text(html, encoding="utf-8")

print("wrote:", out)
print("wrote:", base / "evals" / "trigger_eval.json")
print("trigger count:", sum(1 for e in EVALS if e["should_trigger"]))
print("no-trigger count:", sum(1 for e in EVALS if not e["should_trigger"]))
