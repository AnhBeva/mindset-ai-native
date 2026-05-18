# Module 02: Specification - biến yêu cầu mơ hồ thành đặc tả có thể thực thi

**Bài này giúp người học viết yêu cầu đủ rõ để AI, kỹ sư, tester và reviewer cùng hiểu một việc giống nhau.**

![Nhóm R&D làm rõ yêu cầu trước khi giao AI Agent](assets/visuals/module-02/01-scenario.png)
*Chú thích: Đặc tả tốt bắt đầu trước IDE: team phải thống nhất mục tiêu, ràng buộc, lỗi và tiêu chí Done.*

## 0. Vấn đề thật

“Làm tính năng điều khiển thiết bị” nghe rõ nhưng chưa đủ để thực thi. Nó thiếu user outcome, input/output, source of truth, lỗi, permission, rollback và test.

**Một câu cần nhớ:** Đặc tả không phải giấy tờ; đặc tả là cách giảm đoán mò trước khi hệ thống sinh code.

## 1. Bóc tách bản chất

| Lớp | Câu hỏi | Ý nghĩa |
|---|---|---|
| Mục tiêu | Người dùng cần kết quả gì? | Tránh làm đúng task nhưng sai nhu cầu. |
| Đầu vào/đầu ra | Hệ thống nhận gì và trả gì? | Tránh interface mơ hồ. |
| Lỗi | Điều gì có thể sai? | Tránh happy path only. |
| Ràng buộc | Không được phá gì? | Bảo vệ kiến trúc và sản phẩm cũ. |
| Done | Bằng chứng hoàn thành là gì? | Giúp AI, reviewer, tester cùng chấm. |

![Các lớp của một đặc tả kỹ thuật rõ ràng](assets/visuals/module-02/02-mechanism.png)
*Chú thích: Đặc tả tốt là hợp đồng giữa mục tiêu, dữ liệu, lỗi, ràng buộc và bằng chứng.*

## 2. Nguyên lý cốt lõi

| Nguyên lý | Giải thích | Giới hạn |
|---|---|---|
| Rõ trước khi nhanh | Task càng rõ, AI càng đáng tin. | Không cần viết dài nếu task nhỏ. |
| Error path là một phần yêu cầu | Offline, timeout, thiếu quyền là hành vi sản phẩm. | Không thể phủ mọi lỗi, phải chọn lỗi quan trọng. |
| Done phải đo được | “Chạy ổn” không phải tiêu chí. | Với thử nghiệm sớm, có thể dùng bằng chứng nhẹ hơn. |

## 3. Mô hình tư duy

```text
Goal → Actor → Input → Output → Source of Truth → Error Cases → Constraints → Definition of Done
```

## 4. Quy trình hành động

| Bước | Việc cần làm | Đầu ra | Lỗi thường gặp |
|---|---|---|---|
| 1 | Viết outcome người dùng. | Câu mục tiêu. | Viết “tạo API” thay vì kết quả sản phẩm. |
| 2 | Liệt kê luồng chính và lỗi chính. | Happy/error paths. | Bỏ qua timeout/offline. |
| 3 | Ghi constraint. | Điều không được phá. | Để AI tự refactor rộng. |
| 4 | Viết Done. | Tiêu chí merge. | Done không có test/log. |

![Bài tập viết Definition of Done trước khi code](assets/visuals/module-02/03-workflow-practice.png)
*Chú thích: Definition of Done là điểm neo để AI thực thi và con người review cùng một chuẩn.*

## 5. Case thực chiến

Yêu cầu yếu: “Làm bật đèn phòng khách.”

Yêu cầu tốt hơn: “Cho phép người dùng bật/tắt đèn theo phòng. Nếu thiết bị offline thì không báo thành công. Nếu có nhiều đèn phù hợp thì hỏi lại hoặc dùng rule nhóm. UI chỉ báo thành công khi có confirmed state. Có test cho happy path, offline, timeout, nhiều thiết bị, thiếu quyền.”

## 6. Thực hành

Chọn một yêu cầu mơ hồ trong backlog và viết lại thành đặc tả 8 phần. Reviewer chỉ được chấp nhận khi có ít nhất 3 error case và 1 tiêu chí kiểm chứng rõ.

## 7. Công cụ mang về

Mẫu Definition of Done trong `cong-cu-thuc-hanh-ai-agent.md`.

