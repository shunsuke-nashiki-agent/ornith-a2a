# ornith-a2a — 自律 A2A 開発サンドボックス

GitHub の issue に `agent:go` を付けると、ローカルLLM（Ornith-1.5-35B、GB10常駐）が
**実装 → テスト → PR → レビュー → マージ** を自律で回す実験場。人間は基本 見ているだけ（A2A）。

- 実装役 = Ornith（TAKT オーケストレーション・mac mini 常駐）
- レビュー/マージ役 = Claude（テストが緑の時だけマージ）
- ラベル状態機械: `agent:go` → `agent:doing` → `agent:review`

⚠ サンドボックス専用。自律マージは**このrepoに限定**・**テスト緑が必須ゲート**。
