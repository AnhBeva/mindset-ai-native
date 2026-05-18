# Module 07: Observability và phán đoán kỹ thuật

**Bài này giúp người học nhìn thấy hệ thống khi chạy thật và chọn phương án kỹ thuật phù hợp thay vì chọn phương án trông hay nhất.**

![Dashboard observability cho hệ thống AI-native smart home](assets/visuals/module-07/01-scenario.png)
*Chú thích: Không có log và trace, debug AI Agent giống như sửa hệ thống mà không có đồng hồ đo.*

## 0. Vấn đề thật

Khi hệ thống AI-native sai, lỗi có thể nằm ở user input, speech recognition, intent, context, tool call, device response, state sync hoặc final response. Nếu thiếu observability, team chỉ đoán.

**Một câu cần nhớ:** Hệ thống không quan sát được thì không thể trưởng thành có trách nhiệm.

## 1. Bóc tách bản chất

| Cần nhìn thấy | Câu hỏi | Ý nghĩa |
|---|---|---|
| User input | Người dùng thật sự nói/nhập gì? | Tránh đổ lỗi sai tầng. |
| Intent | AI hiểu mục tiêu gì? | Bắt lỗi hiểu sai. |
| Context | AI nhận bối cảnh nào? | Bắt lỗi context thiếu. |
| Tool call | Tool nào được gọi với tham số gì? | Bắt lỗi action. |
| Tool response | Tool trả gì? | Phân biệt sent/confirmed. |
| Final response | Người dùng được báo gì? | Bắt lỗi nói quá chắc chắn. |

![Trace từ user input đến final response](assets/visuals/module-07/02-mechanism.png)
*Chú thích: Trace tốt giúp team xác định lỗi nằm ở tầng nào thay vì tranh luận bằng cảm giác.*

## 2. Nguyên lý cốt lõi

| Nguyên lý | Giải thích | Dễ sai khi |
|---|---|---|
| Log phải phục vụ câu hỏi debug | Log nhiều chưa chắc hữu ích. | Log không có correlation id. |
| Phán đoán là chọn dưới ràng buộc | AI đưa phương án, con người chọn theo bối cảnh. | Chọn giải pháp phức tạp vì nghe hiện đại. |
| Đơn giản là tài sản vận hành | Càng ít phần chuyển động, càng dễ kiểm chứng. | Tối ưu sớm hoặc over-engineer. |

## 3. Mô hình tư duy

```text
Observe → Localize → Explain → Decide → Verify → Learn
```

## 4. Quy trình hành động

| Bước | Việc cần làm | Đầu ra |
|---|---|---|
| 1 | Gắn correlation id cho luồng quan trọng. | Trace xuyên tầng. |
| 2 | Log input, intent, tool, response, final state. | Dữ liệu debug. |
| 3 | So sánh phương án theo rủi ro. | Quyết định kỹ thuật. |
| 4 | Đo sau release. | Học từ vận hành thật. |

![Bài tập chọn phương án kỹ thuật theo rủi ro và maintainability](assets/visuals/module-07/03-workflow-practice.png)
*Chú thích: Phán đoán kỹ thuật tốt không hỏi “cách nào ngầu hơn”, mà hỏi cách nào đúng bối cảnh, ít rủi ro và dễ kiểm chứng hơn.*

## 5. Case thực chiến

AI đề xuất thêm một service trung gian để xử lý trạng thái thiết bị. Phương án nghe sạch, nhưng team hiện tại thiếu owner vận hành service mới. Phán đoán tốt có thể chọn sửa contract và log hiện tại trước, chỉ tách service khi có rủi ro đủ lớn.

## 6. Thực hành

Lấy 3 phương án AI đề xuất cho một bài toán. Chấm mỗi phương án theo: đơn giản, rủi ro, compatibility, testability, observability, năng lực team.

## 7. Công cụ mang về

Decision table: phương án, lợi ích, rủi ro, điều kiện thành công, test cần có, log cần có, rollback.

