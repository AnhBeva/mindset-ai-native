# Công cụ thực hành AI Agent Cho R&D

## 1. Template giao việc cho AI Agent

```markdown
Bạn là AI coding agent hỗ trợ trong project này.

## Mục tiêu
[Mô tả kết quả sản phẩm cần đạt, không chỉ mô tả code cần viết.]

## Bối cảnh
[Module, flow, lỗi hiện tại, hành vi mong muốn, dữ liệu nguồn sự thật.]

## Phạm vi được phép sửa
- Được sửa:
- Không được sửa:

## Ràng buộc kỹ thuật
- Không thay đổi public API nếu chưa được yêu cầu.
- Không thêm thư viện mới nếu chưa được duyệt.
- Không làm tăng độ phức tạp không cần thiết.
- Tuân thủ convention hiện tại.

## Definition of Done
Task chỉ hoàn thành khi:
1.
2.
3.

## Test bắt buộc
- Happy path:
- Error path:
- Edge case:
- Regression case:

## Yêu cầu đầu ra
1. Tóm tắt nguyên nhân.
2. Tóm tắt thay đổi.
3. Danh sách file đã sửa.
4. Test đã thêm/chạy.
5. Rủi ro còn lại nếu có.
```

## 2. Checklist 5Đ trước khi merge

| 5Đ | Câu hỏi | Bằng chứng cần có |
|---|---|---|
| Đúng vấn đề | Có giải đúng pain point không? | Ticket/brief có mục tiêu và user outcome. |
| Đúng thiết kế | Có giữ boundary, interface, ownership không? | Review kiến trúc hoặc diff nhỏ đúng scope. |
| Đúng dữ liệu | Source of truth, state, input/output rõ chưa? | Contract, schema, confirmed state hoặc trace. |
| Đúng điều kiện lỗi | Offline, timeout, thiếu quyền, trùng tên đã tính chưa? | Test lỗi, fault injection, rollback. |
| Đúng kiểm chứng | Có chứng minh được đúng không? | Test pass, log, benchmark, thiết bị thật nếu cần. |

## 3. Rubric review code do AI sinh

| Tiêu chí | Chưa đạt | Đạt | Xuất sắc |
|---|---|---|---|
| Bám yêu cầu | PR giải vấn đề khác hoặc quá rộng. | Đúng mục tiêu chính. | Đúng mục tiêu, giữ scope, nêu rõ tradeoff. |
| Kiến trúc | Thêm coupling hoặc bypass boundary. | Theo pattern hiện tại. | Làm rõ ownership và giảm rủi ro vận hành. |
| Lỗi và edge case | Chỉ xử lý happy path. | Có error path chính. | Có timeout, permission, rollback, trạng thái không chắc chắn. |
| Test | Ít hoặc không có test. | Có test chính. | Có regression, edge, contract hoặc HIL khi cần. |
| Observability | Không log/trace được lỗi. | Có log cơ bản. | Trace đủ từ input đến tool/device/response. |
| Maintainability | Code dài, khó hiểu, khó sửa. | Dễ đọc và theo convention. | Đơn giản, ít phụ thuộc, dễ mở rộng có kiểm soát. |

## 4. Mẫu Definition of Done cho smart home

```markdown
Task được coi là hoàn thành khi:

1. User có thể bật/tắt thiết bị theo phòng.
2. Nếu thiết bị offline, hệ thống không báo thành công giả.
3. Nếu có nhiều thiết bị phù hợp, hệ thống hỏi lại hoặc dùng rule nhóm đã định nghĩa.
4. UI chỉ báo thành công khi có confirmed state từ backend hoặc thiết bị.
5. Có test cho happy path, offline, timeout, nhiều thiết bị, thiếu quyền.
6. Có log trace từ user command tới intent, tool call, device response và final response.
7. Không thay đổi public API hiện tại nếu chưa được duyệt.
8. Có rollback plan nếu release gây lỗi.
```

## 5. Bài tập chuyển giao

Chọn một task thật trong sprint hiện tại. Viết lại task đó bằng template trên, rồi tự chấm theo 5Đ. Nếu thiếu từ hai chữ Đ trở lên, chưa giao cho AI Agent thực thi.

