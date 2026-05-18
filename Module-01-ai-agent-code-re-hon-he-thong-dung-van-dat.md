# Module 01: AI Agent làm code rẻ hơn, nhưng hệ thống đúng vẫn đắt

**Bài này giúp nhân sự R&D thấy đúng sự dịch chuyển giá trị: từ tự viết từng dòng code sang thiết kế hệ thống thực thi có kiểm chứng.**

![Kỹ sư R&D đứng trước bảng hệ thống cùng AI Agent](assets/visuals/module-01/01-scenario.png)
*Chú thích: Tình huống mở đầu không phải “AI có viết code được không”, mà là team có biết giao đúng việc và kiểm chứng đúng kết quả không.*

## 0. Vấn đề thật trong R&D

AI Agent có thể tạo controller, service, driver mẫu, unit test và tài liệu rất nhanh. Nhưng nếu yêu cầu mơ hồ, kiến trúc không rõ hoặc thiếu kiểm chứng, AI cũng làm nhanh phần sai.

| Khía cạnh | Mô tả |
|---|---|
| Quyền hạn | Người học có thể viết task, review PR, thiết kế API, yêu cầu test. |
| Áp lực | Cần tăng tốc nhưng không được giảm chất lượng sản phẩm. |
| Giới hạn | Legacy code, firmware thật, thiết bị thật, người dùng thật. |
| Hậu quả | Code nhiều hơn nhưng lỗi vào hệ thống nhanh hơn. |

**Một câu cần nhớ:** Code rẻ hơn, nhưng hệ thống đúng vẫn đắt vì đúng vấn đề, đúng kiến trúc và đúng kiểm chứng vẫn cần phán đoán con người.

## 1. Bóc tách bản chất

| Lớp phân tích | Câu hỏi kiểm tra | Nhận định |
|---|---|---|
| Triệu chứng | AI sinh nhiều code nhưng team vẫn mất thời gian sửa. | Tốc độ tạo output tăng nhanh hơn năng lực kiểm soát chất lượng. |
| Nguyên nhân gần | Task thiếu mục tiêu, constraint và test. | AI phải đoán. |
| Nguyên nhân gốc | Team coi AI như máy viết code, không phải lực lượng thực thi cần quản trị. | Thiếu hệ thống giao việc và kiểm chứng. |
| Hệ thống | Review bằng cảm giác, log thiếu, Done không rõ. | Lỗi lọt qua vì không có bằng chứng. |

![Cơ chế code rẻ nhưng quyết định kỹ thuật vẫn đắt](assets/visuals/module-01/02-mechanism.png)
*Chú thích: Khi chi phí sinh code giảm, nút thắt chuyển sang định nghĩa vấn đề, thiết kế hệ thống và kiểm chứng.*

## 2. Nguyên lý cốt lõi

| Nguyên lý | Giải thích | Dễ sai khi |
|---|---|---|
| AI khuếch đại hệ thống hiện có | Quy trình rõ thì AI tăng tốc; quy trình mơ hồ thì AI khuếch đại mơ hồ. | Dùng AI để bỏ qua phân tích. |
| Output không bằng outcome | PR sạch chưa chắc giải đúng vấn đề. | Đánh giá theo số dòng code hoặc tốc độ. |
| Con người giữ trách nhiệm cuối | AI có thể làm, nhưng không chịu trách nhiệm sản phẩm. | Merge vì “AI đã test rồi”. |

## 3. Mô hình tư duy

```text
Mục tiêu sản phẩm → Đặc tả → Kiến trúc → AI thực thi → Kiểm chứng → Release → Học lại quy trình
```

## 4. Quy trình hành động

| Bước | Việc cần làm | Đầu ra |
|---|---|---|
| 1 | Viết mục tiêu sản phẩm trước code. | Outcome rõ. |
| 2 | Nêu ràng buộc và điều không được phá. | Scope an toàn. |
| 3 | Chỉ định bằng chứng đúng. | Test/log/benchmark. |
| 4 | Review bằng 5Đ. | Quyết định merge có lý do. |

![Workflow chuyển từ task sang hệ thống thực thi](assets/visuals/module-01/03-workflow-practice.png)
*Chú thích: Giá trị mới của kỹ sư nằm ở việc thiết kế vòng lặp giúp cả người và AI cùng làm đúng nhanh hơn.*

## 5. Case thực chiến

Team giao AI “tối ưu luồng điều khiển đèn”. AI sửa nhanh, test pass, nhưng sau release có thiết bị offline vẫn báo thành công. Vấn đề thật không phải thiếu code tối ưu; vấn đề là task không định nghĩa confirmed state, error path và log trace.

## 6. Thực hành có phản hồi

Viết lại một task gần đây theo cấu trúc: mục tiêu, bối cảnh, scope, ràng buộc, Definition of Done, test bắt buộc, rủi ro còn lại.

| Tiêu chí | Chưa đạt | Đạt | Xuất sắc |
|---|---|---|---|
| Mục tiêu | Chỉ nêu việc code. | Có outcome. | Có outcome và tiêu chí đo. |
| Scope | Mơ hồ. | Có phạm vi sửa. | Có cả điều không được đổi. |
| Kiểm chứng | Không rõ. | Có test. | Có test, log và rollback. |

## 7. Công cụ mang về

Dùng checklist 5Đ trong `cong-cu-thuc-hanh-ai-agent.md` trước khi giao AI làm task quan trọng.

