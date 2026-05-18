# Bản đồ AI Native Agent Mindset Cho R&D

## 1. Lĩnh vực này thực sự là gì?

AI Native Agent Mindset là năng lực thiết kế cách con người, AI Agent, codebase, tool, test, log và quy trình cùng tạo ra kết quả kỹ thuật đúng. Trọng tâm không phải là “dùng AI cho nhanh”, mà là biến tốc độ của AI thành năng lực thực thi an toàn, có kiến trúc và có bằng chứng.

## 2. Các câu hỏi cốt lõi

| Câu hỏi | Vì sao quan trọng | Nếu không trả lời được sẽ nhầm gì? |
|---|---|---|
| Vấn đề thật là gì? | AI chỉ hữu ích khi mục tiêu đúng. | Sinh code giải nhầm pain point. |
| Ràng buộc nào không được phá? | R&D thường có legacy, firmware, tài nguyên, safety. | Tạo PR sạch nhưng làm hệ thống khó vận hành. |
| Hệ thống nên chia thế nào? | AI giỏi làm từng mảnh, nhưng cần mảnh đúng. | Nhân bản sự rối trong kiến trúc. |
| Kết quả đúng được chứng minh bằng gì? | Cảm giác “trông ổn” không đủ để release. | Release lỗi không có test, log hoặc rollback. |
| AI được phép làm gì và không được làm gì? | Agent có tốc độ cao nên cần đường ray. | Tự ý sửa ngoài scope hoặc thay đổi public contract. |

## 3. Nguyên tắc phân chia

| Tầng | Câu hỏi cốt lõi | Nhánh/mô hình tiêu biểu | Ý nghĩa thực tiễn |
|---|---|---|---|
| Purpose | Ta cần tạo giá trị gì? | Từ coder sang người thiết kế hệ thống thực thi. | Giữ vai trò con người ở định nghĩa, kiến trúc, kiểm chứng. |
| Specification | Task có đủ rõ để làm đúng chưa? | Goal, scope, constraint, Definition of Done. | Giảm mơ hồ trước khi AI sinh code. |
| Context | AI cần biết gì để không đoán mò? | Context Engineering, file liên quan, coding convention. | Tăng chất lượng output và giảm sửa lại. |
| Architecture | Hệ thống được chia và nối thế nào? | Boundary, interface, state, error flow, ownership. | Giúp AI làm nhanh nhưng không phá thiết kế. |
| Tool/API | AI sẽ hành động qua interface nào? | Tool rõ intent, enum, permission, confirmed state. | Giảm gọi nhầm, báo thành công giả, thao tác rủi ro. |
| Evaluation | Bằng chứng đúng là gì? | Test, log, trace, benchmark, HIL, fault injection. | Chuyển từ cảm giác sang kiểm chứng. |
| Operations | Team vận hành AI thế nào? | 5Đ, checklist review, approval, rollback. | Biến cá nhân dùng AI thành năng lực team. |

## 4. Bản đồ năng lực

| Nhánh | Bản chất | Dấu hiệu đạt | Ứng dụng |
|---|---|---|---|
| Đặc tả | Biến mơ hồ thành tiêu chí thực thi. | Task có mục tiêu, lỗi, ràng buộc, Done. | Brief cho AI, ticket, PR scope. |
| Kiến trúc | Chia hệ thống theo trách nhiệm và dòng dữ liệu. | Module, interface, state, log và ownership rõ. | Review thiết kế trước khi sinh code. |
| Kiểm chứng | Chứng minh hệ thống đúng trong điều kiện thật. | Có test, log, trace, metric, case lỗi. | Release, regression, firmware validation. |
| Phán đoán | Chọn phương án phù hợp bối cảnh. | Biết đánh đổi đơn giản, rủi ro, maintainability. | Quyết định giữa 5 phương án AI đề xuất. |
| Quản trị Agent | Dùng AI như lực lượng thực thi có kiểm soát. | Scope, context, approval, rollback, review. | Tăng tốc mà không mất kiểm soát chất lượng. |

## 5. Mô hình nhớ nhanh: 5Đ

| 5Đ | Câu hỏi kiểm tra |
|---|---|
| Đúng vấn đề | Có đang giải đúng pain point không? |
| Đúng thiết kế | Kiến trúc, module, interface có hợp lý không? |
| Đúng dữ liệu | Input, output, state, source of truth có rõ không? |
| Đúng điều kiện lỗi | Offline, timeout, mất gói, trùng tên, thiếu quyền đã xử lý chưa? |
| Đúng kiểm chứng | Có test, log, benchmark hoặc bằng chứng để chứng minh không? |

