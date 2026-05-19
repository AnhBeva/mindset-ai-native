#!/usr/bin/env python3
from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent

DOCS = [
    ("README.md", "Tổng quan"),
    ("ban-do-ai-native-agent-mindset.md", "Bản đồ"),
    ("giao-trinh-ai-native-agent-mindset.md", "Giáo trình"),
    ("thuat-ngu-ai-native-agent-mindset.md", "Thuật ngữ"),
    ("Module-01-ai-agent-code-re-hon-he-thong-dung-van-dat.md", "01. Code rẻ, hệ thống đúng vẫn đắt"),
    ("Module-02-specification-dac-ta-co-the-thuc-thi.md", "02. Specification: đặc tả thực thi"),
    ("Module-03-context-engineering-giao-viec-cho-ai.md", "03. Context Engineering cho AI"),
    ("Module-04-architecture-chia-he-thong-dung.md", "04. Architecture: chia hệ thống đúng"),
    ("Module-05-tool-api-design-tay-chan-an-toan.md", "05. Tool/API Design an toàn"),
    ("Module-06-evaluation-bang-chung-dung.md", "06. Evaluation: bằng chứng đúng"),
    ("Module-07-observability-phan-doan-ky-thuat.md", "07. Observability & phán đoán"),
    ("Module-08-operating-system-team-rd-ai-native.md", "08. Operating System cho team"),
    ("cong-cu-thuc-hanh-ai-agent.md", "Công cụ"),
]


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[àáạảãâầấậẩẫăằắặẳẵ]", "a", text)
    text = re.sub(r"[èéẹẻẽêềếệểễ]", "e", text)
    text = re.sub(r"[ìíịỉĩ]", "i", text)
    text = re.sub(r"[òóọỏõôồốộổỗơờớợởỡ]", "o", text)
    text = re.sub(r"[ùúụủũưừứựửữ]", "u", text)
    text = re.sub(r"[ỳýỵỷỹ]", "y", text)
    text = text.replace("đ", "d")
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "section"


def parse_inline(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', escaped)
    return escaped


def render_table(lines: list[str]) -> str:
    rows = []
    for line in lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        rows.append(cells)
    if len(rows) > 1 and all(set(cell) <= {"-", ":"} for cell in rows[1]):
        header = rows[0]
        body = rows[2:]
    else:
        header = []
        body = rows
    out = ['<div class="table-wrap"><table>']
    if header:
        out.append("<thead><tr>" + "".join(f"<th>{parse_inline(c)}</th>" for c in header) + "</tr></thead>")
    out.append("<tbody>")
    for row in body:
        out.append("<tr>" + "".join(f"<td>{parse_inline(c)}</td>" for c in row) + "</tr>")
    out.append("</tbody></table></div>")
    return "\n".join(out)


def render_markdown(md: str, doc_id: str) -> tuple[str, str]:
    lines = md.splitlines()
    out: list[str] = []
    title = doc_id
    i = 0
    in_ul = False
    in_ol = False

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            close_lists()
            i += 1
            continue
        if stripped.startswith("```"):
            close_lists()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            out.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
            i += 1
            continue
        if stripped.startswith("|") and "|" in stripped[1:]:
            close_lists()
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            out.append(render_table(table_lines))
            continue
        image = re.match(r"!\[([^\]]*)\]\(([^)]+)\)", stripped)
        if image:
            close_lists()
            alt, src = image.groups()
            caption = ""
            if i + 1 < len(lines) and (
                lines[i + 1].strip().startswith("*Caption:")
                or lines[i + 1].strip().startswith("*Chú thích:")
            ):
                caption = lines[i + 1].strip().strip("*")
                i += 1
            out.append(
                f'<figure><img src="{html.escape(src)}" alt="{html.escape(alt)}">'
                f"<figcaption>{parse_inline(caption) if caption else html.escape(alt)}</figcaption></figure>"
            )
            i += 1
            continue
        heading = re.match(r"^(#{1,3})\s+(.+)$", stripped)
        if heading:
            close_lists()
            level = len(heading.group(1))
            text = heading.group(2)
            if level == 1:
                title = text
            hid = f"{doc_id}-{slugify(text)}"
            out.append(f'<h{level} id="{hid}">{parse_inline(text)}</h{level}>')
            i += 1
            continue
        if stripped.startswith(">"):
            close_lists()
            out.append(f"<blockquote>{parse_inline(stripped.lstrip('> ').strip())}</blockquote>")
            i += 1
            continue
        if re.match(r"^[-*]\s+", stripped):
            if not in_ul:
                close_lists()
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{parse_inline(re.sub(r'^[-*]\\s+', '', stripped))}</li>")
            i += 1
            continue
        if re.match(r"^\d+\.\s+", stripped):
            if not in_ol:
                close_lists()
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{parse_inline(re.sub(r'^\\d+\\.\\s+', '', stripped))}</li>")
            i += 1
            continue
        close_lists()
        out.append(f"<p>{parse_inline(stripped)}</p>")
        i += 1
    close_lists()
    return title, "\n".join(out)


def build() -> None:
    sections = []
    nav = []
    for filename, label in DOCS:
        path = ROOT / filename
        doc_id = slugify(filename.rsplit(".", 1)[0])
        title, body = render_markdown(path.read_text(encoding="utf-8"), doc_id)
        nav.append(f'<a href="#doc-{doc_id}">{html.escape(label)}</a>')
        sections.append(f'<section class="doc-section" id="doc-{doc_id}"><div class="section-label">{html.escape(label)}</div>{body}</section>')

    html_text = f"""<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>AI Native Agent Mindset Cho R&D</title>
  <meta name="description" content="Nền tảng học tập Lumi-branded về tư duy AI Native Agent cho nhân sự R&D.">
  <style>
    :root {{
      --lumi-green: #008B51;
      --lumi-green-deep: #006B3F;
      --lumi-mint: #E6F4EE;
      --lumi-pale: #F3FAF6;
      --text: #1F2933;
      --muted: #4B5563;
      --line: #DDE5E1;
      --surface: #FFFFFF;
      --accent: #F3B23C;
    }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      margin: 0;
      font-family: Arial, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: var(--text);
      background: var(--lumi-pale);
      line-height: 1.68;
      letter-spacing: 0;
    }}
    img {{ max-width: 100%; display: block; }}
    a {{ color: var(--lumi-green-deep); }}
    .shell {{
      display: grid;
      grid-template-columns: 330px minmax(0, 1fr);
      min-height: 100vh;
    }}
    .sidebar {{
      position: sticky;
      top: 0;
      height: 100vh;
      overflow: auto;
      padding: 22px 18px;
      border-right: 1px solid var(--line);
      background: rgba(255,255,255,.92);
    }}
    .brand-logo {{
      display: block;
      height: 42px;
      width: auto;
      object-fit: contain;
      margin-bottom: 18px;
    }}
    .platform-label {{
      color: var(--lumi-green-deep);
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      margin: 10px 0 4px;
    }}
    .sidebar h1 {{
      font-size: 22px;
      line-height: 1.18;
      margin: 0 0 18px;
      letter-spacing: 0;
    }}
    nav {{
      display: grid;
      gap: 4px;
      margin-top: 16px;
    }}
    nav a {{
      padding: 9px 10px;
      border-radius: 8px;
      text-decoration: none;
      color: var(--text);
      font-size: 13.5px;
      line-height: 1.28;
      font-weight: 700;
      overflow-wrap: anywhere;
    }}
    nav a:hover {{ background: var(--lumi-mint); color: var(--lumi-green-deep); }}
    main {{
      min-width: 0;
      padding: 0 0 72px;
    }}
    .hero {{
      min-height: 88vh;
      display: grid;
      align-items: end;
      padding: 48px clamp(22px, 5vw, 72px);
      background:
        linear-gradient(90deg, rgba(255,255,255,.98) 0%, rgba(255,255,255,.86) 46%, rgba(255,255,255,.42) 100%),
        url('assets/ai-native-rd-hero.png') center/cover no-repeat;
      border-bottom: 1px solid var(--line);
    }}
    .hero-inner {{ max-width: 900px; }}
    .eyebrow {{ color: var(--lumi-green); font-weight: 800; margin: 0 0 12px; }}
    .hero h2 {{
      margin: 0;
      font-size: clamp(38px, 6vw, 78px);
      line-height: 1.02;
      letter-spacing: 0;
      max-width: 920px;
    }}
    .lead {{
      max-width: 760px;
      font-size: clamp(18px, 2vw, 24px);
      color: var(--muted);
      margin: 22px 0 0;
    }}
    .stats {{
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 12px;
      margin-top: 30px;
      max-width: 760px;
    }}
    .stat {{
      background: rgba(255,255,255,.86);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 14px;
    }}
    .stat strong {{ display: block; color: var(--lumi-green-deep); font-size: 24px; line-height: 1; }}
    .stat span {{ color: var(--muted); font-size: 13px; font-weight: 700; }}
    .doc-section {{
      width: min(980px, calc(100% - 44px));
      margin: 34px auto 0;
      padding: clamp(24px, 4vw, 44px);
      background: var(--surface);
      border: 1px solid var(--line);
      border-radius: 8px;
    }}
    .section-label {{
      display: inline-flex;
      color: var(--lumi-green-deep);
      background: var(--lumi-mint);
      border: 1px solid #C9E8D9;
      border-radius: 999px;
      padding: 4px 10px;
      font-size: 12px;
      font-weight: 800;
      margin-bottom: 16px;
    }}
    h1, h2, h3 {{ line-height: 1.2; letter-spacing: 0; }}
    .doc-section h1 {{ margin: 0 0 18px; font-size: clamp(30px, 4vw, 46px); }}
    .doc-section h2 {{ margin-top: 34px; font-size: clamp(24px, 3vw, 34px); }}
    .doc-section h3 {{ margin-top: 28px; font-size: 22px; }}
    p, li {{ font-size: 17px; }}
    blockquote {{
      margin: 22px 0;
      padding: 16px 18px;
      border-left: 4px solid var(--lumi-green);
      background: var(--lumi-mint);
      font-weight: 700;
    }}
    figure {{
      margin: 28px 0;
      border: 1px solid var(--line);
      border-radius: 8px;
      overflow: hidden;
      background: #fff;
    }}
    figure img {{
      width: 100%;
      aspect-ratio: 16 / 9;
      object-fit: cover;
    }}
    figcaption {{
      padding: 12px 14px;
      color: var(--muted);
      font-size: 14px;
      background: #fff;
      border-top: 1px solid var(--line);
    }}
    .table-wrap {{
      overflow-x: auto;
      margin: 22px 0;
      border: 1px solid var(--line);
      border-radius: 8px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      min-width: 680px;
      background: #fff;
    }}
    th, td {{
      border-bottom: 1px solid var(--line);
      padding: 11px 12px;
      text-align: left;
      vertical-align: top;
    }}
    th {{
      color: var(--lumi-green-deep);
      background: var(--lumi-mint);
      font-size: 14px;
    }}
    tr:last-child td {{ border-bottom: 0; }}
    code {{
      background: #EEF6F2;
      border: 1px solid #D5EADF;
      border-radius: 6px;
      padding: 1px 5px;
      font-size: .92em;
    }}
    pre {{
      overflow: auto;
      padding: 16px;
      border-radius: 8px;
      background: #14251D;
      color: #E8FFF2;
    }}
    pre code {{ background: transparent; border: 0; color: inherit; padding: 0; }}
    @media (max-width: 920px) {{
      .shell {{ display: block; }}
      .sidebar {{
        position: static;
        height: auto;
        border-right: 0;
        border-bottom: 1px solid var(--line);
      }}
      .brand-logo {{ height: 34px; }}
      nav {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
      .hero {{ min-height: auto; padding-top: 56px; }}
      .stats {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
    }}
    @media (max-width: 560px) {{
      nav {{ grid-template-columns: 1fr; }}
      .stats {{ grid-template-columns: 1fr; }}
      .doc-section {{ width: calc(100% - 24px); padding: 18px; }}
      p, li {{ font-size: 16px; }}
      table {{ min-width: 620px; }}
    }}
    @media print {{
      .sidebar {{ display: none; }}
      .shell {{ display: block; }}
      .hero {{ min-height: auto; background: #fff; }}
      .doc-section {{ border: 0; width: 100%; page-break-inside: avoid; }}
    }}
  </style>
</head>
<body>
  <div class="shell">
    <aside class="sidebar">
      <img class="brand-logo" src="assets/lumi-logo-2022.png" alt="Lumi">
      <div class="platform-label">Nền tảng học tập ứng dụng</div>
      <h1>AI Native Agent Mindset Cho R&D</h1>
      <nav aria-label="Điều hướng nội dung">
        {chr(10).join(nav)}
      </nav>
    </aside>
    <main>
      <section class="hero">
        <div class="hero-inner">
          <p class="eyebrow">Lumi R&D Learning Platform</p>
          <h2>Từ coder sang người thiết kế hệ thống thực thi có kiểm chứng</h2>
          <p class="lead">Một nền tảng học tập giúp Software Engineer, Firmware Engineer, Tester, BA, PM và Leader dùng AI Agent như lực lượng thực thi mạnh nhưng có đường ray kỹ thuật rõ.</p>
          <div class="stats">
            <div class="stat"><strong>8</strong><span>module ứng dụng</span></div>
            <div class="stat"><strong>24</strong><span>visual học tập</span></div>
            <div class="stat"><strong>5Đ</strong><span>bộ lọc chất lượng</span></div>
            <div class="stat"><strong>30</strong><span>ngày nâng cấp team</span></div>
          </div>
        </div>
      </section>
      {chr(10).join(sections)}
    </main>
  </div>
</body>
</html>
"""
    (ROOT / "index.html").write_text(html_text, encoding="utf-8")


if __name__ == "__main__":
    build()
