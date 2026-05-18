# Thuật ngữ AI Native Agent Mindset

| Thuật ngữ | Nhóm | Định nghĩa ngắn | Bản chất | Câu hỏi ứng dụng |
|---|---|---|---|---|
| AI Agent | Nền tảng | Hệ thống AI có thể lập kế hoạch, đọc file, gọi tool, sửa code, chạy lệnh và lặp lại. | Một lực lượng thực thi nhanh cần được định hướng và kiểm chứng. | Agent được phép làm gì trong task này? |
| Specification | Đặc tả | Mô tả mục tiêu, ràng buộc, đầu vào, đầu ra, lỗi và tiêu chí hoàn thành. | Biến mơ hồ thành điều có thể thực thi. | Task này đã đủ rõ để AI không đoán mò chưa? |
| Definition of Done | Đặc tả | Danh sách điều kiện để coi task hoàn thành. | Hợp đồng chất lượng trước khi code. | Bằng chứng nào cho thấy Done thật sự đạt? |
| Context Engineering | Giao việc cho AI | Thiết kế ngữ cảnh AI cần để hành động đúng. | Prompt chỉ là phần nổi; context quyết định chất lượng. | AI cần biết file, convention, ràng buộc và điều cấm nào? |
| Architecture Boundary | Kiến trúc | Ranh giới trách nhiệm giữa module hoặc tầng hệ thống. | Giảm coupling và giúp AI sửa đúng chỗ. | Thay đổi này thuộc module nào và không được lan sang đâu? |
| Source of Truth | Dữ liệu | Nơi có thẩm quyền cuối cùng về trạng thái hoặc dữ liệu. | Tránh nhiều bản thật cạnh tranh nhau. | UI đang tin backend, cache hay thiết bị thật? |
| Confirmed State | Điều khiển thiết bị | Trạng thái đã được xác nhận bởi nguồn thật, không chỉ lệnh đã gửi. | Không báo thành công giả. | Khi nào được nói “đã bật”? |
| Evaluation | Kiểm chứng | Cách chứng minh kết quả đúng bằng test, log, benchmark hoặc bằng chứng thật. | Chuyển từ cảm giác sang bằng chứng. | Test/log nào sẽ bắt lỗi nếu AI làm sai? |
| Observability | Vận hành | Khả năng nhìn thấy hệ thống đang làm gì qua log, trace, metric. | Không đo được thì khó debug và cải tiến. | Lỗi nằm ở intent, tool, device hay response? |
| Hardware-in-the-loop | Firmware | Kiểm thử có thiết bị thật trong vòng kiểm chứng. | Mock không thay thế được hành vi vật lý. | Code này đã chạy trên thiết bị thật chưa? |
| Fault Injection | Kiểm chứng | Cố ý tạo lỗi như timeout, mất gói, offline, reboot để kiểm tra hệ thống. | Hệ thống tốt phải biết sai an toàn. | Ta đã thử tình huống xấu trước release chưa? |
| 5Đ | Quy trình | Đúng vấn đề, đúng thiết kế, đúng dữ liệu, đúng điều kiện lỗi, đúng kiểm chứng. | Bộ lọc chất lượng trước khi tin một task đã xong. | Task này thiếu chữ Đ nào? |

