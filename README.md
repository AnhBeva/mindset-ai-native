# AI Native Agent Mindset Cho R&D

Nền tảng này giúp nhân sự R&D của Lumi/AND chuyển từ tư duy “làm task và viết code” sang tư duy **thiết kế hệ thống thực thi có kiểm chứng** trong thời AI Agent.

## Lời hứa học tập

Sau khi học, người học có thể:

- Biến yêu cầu mơ hồ thành đặc tả rõ, có ràng buộc và Definition of Done.
- Chia hệ thống thành module, interface, state, error flow và ownership đủ rõ để con người lẫn AI cùng thực thi.
- Thiết kế context, tool/API và phạm vi an toàn khi giao việc cho AI Agent.
- Review code do AI sinh bằng tiêu chí kỹ thuật thay vì cảm giác.
- Chứng minh kết quả đúng bằng test, log, trace, benchmark hoặc bằng chứng trên thiết bị thật.
- Dùng mô hình 5Đ để nâng cấp quy trình làm việc của cả team R&D.

## Đối tượng

Software Engineer, Firmware Engineer, Tester, BA, PM, Leader và các vai trò R&D đang xây sản phẩm công nghệ, smart home, IoT hoặc hệ thống có AI Agent tham gia vào quy trình phát triển.

## Cấu trúc

| Tài liệu | Vai trò |
|---|---|
| `ban-do-ai-native-agent-mindset.md` | Bản đồ lĩnh vực và các tầng năng lực. |
| `giao-trinh-ai-native-agent-mindset.md` | Lộ trình học theo module và mục tiêu ứng dụng. |
| `thuat-ngu-ai-native-agent-mindset.md` | Thuật ngữ cốt lõi để team dùng chung ngôn ngữ. |
| `Module-01` đến `Module-08` | Bài học ứng dụng theo tình huống R&D. |
| `cong-cu-thuc-hanh-ai-agent.md` | Checklist, template prompt, Definition of Done và review rubric. |
| `build_platform_html.py` | Script dựng website tĩnh từ Markdown nguồn. |
| `index.html` | Website học tập tĩnh đã build. |

## Build local

```bash
python3 build_platform_html.py
```

Sau khi build, mở `index.html` trực tiếp trong trình duyệt hoặc chạy:

```bash
python3 -m http.server 8000
```

## Nguồn

Nội dung được xây từ `bai_chia_se_ai_native_agent_mindset.md` và mở rộng thành nền tảng học tập ứng dụng. Tài liệu nguồn gốc được giữ nguyên.

