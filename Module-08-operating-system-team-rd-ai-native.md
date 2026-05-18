# Module 08: Operating System cho team R&D AI-native

**Bài này giúp leader và team biến AI-native mindset thành thói quen vận hành hằng ngày, không chỉ là kỹ năng cá nhân.**

![Team R&D dùng checklist 5Đ trong buổi review sprint](assets/visuals/module-08/01-scenario.png)
*Chú thích: AI-native không chỉ là dùng công cụ mới; đó là cách team định nghĩa, thực thi, kiểm chứng và học lại.*

## 0. Vấn đề thật

Nếu mỗi người dùng AI theo cách riêng, chất lượng sẽ phụ thuộc vào cá nhân. Team cần một operating system chung: task brief, context, review, test, log, approval, rollback và learning loop.

**Một câu cần nhớ:** Giá trị cao nhất là biến AI thành năng lực tổ chức, không chỉ năng suất cá nhân.

## 1. Bóc tách bản chất

| Tầng vận hành | Câu hỏi | Dấu hiệu đạt |
|---|---|---|
| Trước khi làm | Task có mục tiêu, scope, Done chưa? | Không giao việc mơ hồ. |
| Khi dùng AI | Context và quyền sửa rõ chưa? | AI tạo diff đúng phạm vi. |
| Khi review | Có đối chiếu 5Đ không? | Không merge bằng cảm giác. |
| Trước release | Có rollback và monitor không? | Release có kiểm soát. |
| Sau release | Có ghi lại bài học không? | Team làm lần sau tốt hơn. |

![Mô hình 5Đ như hệ điều hành chất lượng cho team](assets/visuals/module-08/02-mechanism.png)
*Chú thích: 5Đ giúp team có cùng bộ lọc chất lượng trước khi tin rằng một task đã xong.*

## 2. Nguyên lý cốt lõi

| Nguyên lý | Giải thích | Dễ sai khi |
|---|---|---|
| Quy trình tốt làm AI mạnh hơn | AI cần đường ray để chạy nhanh. | Thả AI tự do vào production code. |
| Checklist là bộ nhớ tổ chức | Giảm phụ thuộc vào người nhớ giỏi. | Checklist quá dài và không dùng thật. |
| Học sau release là bắt buộc | Mỗi lỗi nên nâng cấp quy trình. | Chỉ sửa lỗi rồi quên pattern. |

## 3. Mô hình tư duy

```text
Task Brief → AI Execution → Human Review → Evidence → Release → Monitor → Retrospective → Better Template
```

## 4. Quy trình hành động

| Tuần | Trọng tâm | Kết quả |
|---|---|---|
| 1 | Viết task rõ. | Mỗi task có goal, scope, constraint, Done. |
| 2 | Dùng AI có kiểm soát. | Prompt có context, phạm vi, test. |
| 3 | Thiết kế test và log. | Mỗi task có bằng chứng đúng. |
| 4 | Cải tiến quy trình team. | Checklist review, template task, bug pattern. |

![Lộ trình 30 ngày nâng cấp team R&D AI-native](assets/visuals/module-08/03-workflow-practice.png)
*Chú thích: Lộ trình tốt bắt đầu từ task thật, tạo thói quen thật và đo bằng chất lượng công việc thật.*

## 5. Case thực chiến

Sau một lỗi offline báo thành công, team không chỉ sửa bug. Team cập nhật template task để luôn hỏi confirmed state, thêm test timeout/offline vào checklist, bổ sung log correlation id và thêm mục “source of truth” vào review.

## 6. Thực hành

Chọn một lỗi production hoặc bug pattern gần đây. Viết “bài học quy trình”: lỗi lọt qua vì thiếu chữ Đ nào, template nào cần sửa, test/log nào cần thêm, ai chịu trách nhiệm áp dụng.

## 7. Công cụ mang về

Một operating system tối thiểu cho team: task template, 5Đ review, AI scope policy, required evidence, release checklist, retrospective learning log.

