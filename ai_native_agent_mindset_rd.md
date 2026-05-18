# Khi AI biết code, nhân sự R&D còn phải giỏi điều gì?

![Kỹ sư R&D điều phối AI Agent trong một phòng lab hiện đại](assets/ai-native-rd-hero.png)

Có một nghịch lý đang đến rất nhanh với các phòng R&D.

Chúng ta từng nghĩ người giỏi là người viết code nhanh, xử lý task nhanh, nhớ framework tốt, debug dai sức. Nhưng bây giờ, một AI Agent có thể đọc project, sửa file, tạo test, viết tài liệu, chạy lệnh, nhìn log, rồi tự lặp lại cho đến khi mọi thứ có vẻ ổn. Một task mà trước đây cần vài giờ, thậm chí vài ngày, có thể được AI tạo ra bản nháp trong vài phút.

Nghe như một tin rất tốt. Nhưng cũng là một câu hỏi hơi khó chịu:

> Nếu AI đã viết code nhanh hơn, đọc tài liệu nhanh hơn, tạo test nhanh hơn, vậy giá trị thật sự của nhân sự R&D còn nằm ở đâu?

Câu trả lời không phải là: chúng ta phải gõ phím nhanh hơn AI.

Cũng không phải là: chúng ta phải né AI để giữ lại vai trò cũ.

Câu trả lời thực tế hơn là: vai trò của chúng ta phải dịch chuyển. Từ người trực tiếp làm từng mảnh việc, sang người biết định nghĩa đúng vấn đề, thiết kế đúng hệ thống, đặt đúng ràng buộc, kiểm chứng đúng kết quả, và dùng AI như một lực lượng thực thi rất mạnh nhưng cần được dẫn dắt.

AI Agent không làm kỹ sư giỏi trở nên kém quan trọng. Nó làm cho sự khác biệt giữa người hiểu hệ thống và người chỉ làm theo task trở nên rõ hơn.

Vì AI có một đặc điểm rất mạnh, nhưng cũng rất nguy hiểm: nó làm nhanh cả việc đúng lẫn việc sai.

Nếu yêu cầu mơ hồ, AI có thể sinh ra rất nhiều code mơ hồ. Nếu kiến trúc không rõ, AI có thể làm hệ thống rối nhanh hơn. Nếu không có tiêu chí kiểm chứng, chúng ta rất dễ nhầm giữa “trông có vẻ đúng” và “đúng thật”.

Đó là lý do phòng R&D trong thời AI-native không chỉ cần học cách dùng AI. Chúng ta cần học cách nghĩ lại về công việc kỹ thuật.

## Vấn đề không còn là ai viết code nhanh hơn

Trước đây, phần tốn sức nhất thường là viết code. Có yêu cầu, kỹ sư phân tích, viết code, test, sửa lỗi, release. Tốc độ cá nhân ảnh hưởng rất lớn đến tiến độ.

Bây giờ, chi phí sinh code đang giảm rất nhanh. AI có thể viết controller, service, driver mẫu, unit test, migration, tài liệu API, checklist review. Nhưng hệ thống đúng vẫn không hề rẻ.

Code rẻ hơn. Nhưng hiểu đúng vấn đề vẫn đắt. Kiến trúc đúng vẫn đắt. Debug trên thiết bị thật vẫn đắt. Test đúng case lỗi vẫn đắt. Quyết định kỹ thuật sai vẫn rất đắt.

Một sản phẩm không thất bại vì thiếu vài dòng code. Nó thường thất bại vì chúng ta hiểu sai yêu cầu, chia sai module, đặt sai source of truth, không xử lý case lỗi, log không đủ để truy vết, hoặc release một thay đổi mà không biết làm sao chứng minh nó tốt hơn.

Trong thời AI Agent, câu hỏi trung tâm không còn là:

> Làm sao để viết nhanh hơn?

Mà là:

> Làm sao để định nghĩa đúng hơn, thiết kế rõ hơn, kiểm chứng chắc hơn, và để cả con người lẫn AI cùng thực thi an toàn hơn?

![Dòng chảy từ đặc tả, kiến trúc đến kiểm chứng](assets/spec-architecture-evaluation.png)

Nếu chỉ nhớ một mô hình, hãy nhớ ba từ này:

**Đặc tả. Kiến trúc. Kiểm chứng.**

Đặc tả là biến một yêu cầu mơ hồ thành một mục tiêu rõ ràng. Kiến trúc là chia hệ thống thành những phần có boundary, interface, state và trách nhiệm rõ. Kiểm chứng là bằng chứng cho thấy kết quả đúng, không chỉ cảm giác rằng nó ổn.

Ba năng lực này tạo thành vòng lặp cốt lõi của nhân sự R&D trong thời AI-native.

## Một yêu cầu đơn giản có thể che giấu cả một hệ thống phức tạp

Hãy lấy một ví dụ rất gần với sản phẩm công nghệ: người dùng nói “bật đèn phòng khách”.

Nghe như một câu lệnh rất đơn giản. Nếu giao cho AI hoặc một kỹ sư junior, có thể họ sẽ nghĩ: nhận câu nói, tìm thiết bị, gửi lệnh bật, báo thành công.

Nhưng hệ thống thật không đơn giản như vậy.

Người dùng nói bằng giọng nào? Nhận diện có đúng không? “Phòng khách” là phòng nào nếu nhà có nhiều tầng? Có một đèn hay nhiều đèn? “Đèn phòng khách” là thiết bị, nhóm thiết bị, hay một scene? Thiết bị có online không? Backend có nhận lệnh không? Thiết bị có phản hồi trạng thái thật không? Nếu gửi lệnh thành công nhưng thiết bị không đổi trạng thái thì có được báo “đã bật” không? Nếu người dùng không có quyền điều khiển thiết bị đó thì sao? Log nào giúp team biết lỗi nằm ở nhận diện giọng nói, mapping thiết bị, tool call, gateway, hay firmware?

Một câu lệnh người dùng chỉ có vài chữ, nhưng phía sau là cả chuỗi kỹ thuật:

Âm thanh → văn bản → ý định → thiết bị/phòng/scene → tool call → phản hồi thiết bị → trạng thái xác nhận → phản hồi cho người dùng.

Kỹ sư giỏi trong thời AI-native là người nhìn thấy toàn chuỗi đó. Không chỉ nhìn thấy một function.

Và khi giao việc cho AI, người đó không nói:

> Làm tính năng bật đèn.

Họ nói rõ hơn:

> Cho phép người dùng bật/tắt đèn theo phòng. Nếu thiết bị offline thì không được báo thành công. Nếu có nhiều thiết bị phù hợp thì phải hỏi lại hoặc xử lý theo rule nhóm đã định nghĩa. UI chỉ hiển thị thành công khi có confirmed state từ backend. Cần test cho happy path, offline, timeout, nhiều thiết bị, thiếu quyền. Không thay đổi public API hiện tại. Cần log trace từ user command tới tool call và phản hồi thiết bị.

Khác biệt không nằm ở độ dài câu chữ. Khác biệt nằm ở chất lượng tư duy.

AI rất mạnh khi bài toán rõ. AI rất nguy hiểm khi bài toán mơ hồ nhưng người review lại dễ bị thuyết phục bởi một pull request trông sạch.

## AI Agent giống một nhân sự rất nhanh, không phải một người chịu trách nhiệm thay ta

Nhiều người vẫn hiểu AI như một công cụ hỏi đáp: viết giúp tôi hàm này, giải thích đoạn code kia, tạo giúp tôi unit test. Nhưng AI Agent đã đi xa hơn. Nó có thể đọc file, lập kế hoạch, gọi tool, sửa code, chạy test, đọc log, tự sửa tiếp.

Vì vậy, cách quản trị AI Agent cũng phải khác cách dùng một chatbot.

Một hình dung thực tế là: AI Agent giống một nhân sự junior có tốc độ cực cao. Nó đọc nhanh, viết nhanh, không mệt, chịu làm việc lặp lại. Nhưng nó vẫn cần người senior định hướng, giới hạn phạm vi, kiểm tra rủi ro, và chịu trách nhiệm cuối cùng.

Nếu giao cho một junior yêu cầu mơ hồ, ta không nên ngạc nhiên khi kết quả lệch. Với AI cũng vậy. Chỉ khác là AI có thể tạo ra kết quả lệch với tốc độ rất cao và hình thức rất thuyết phục.

Vì vậy, câu hỏi trước khi dùng AI không phải là “AI có làm được không?”. Câu hỏi đúng hơn là:

> Ta đã đủ rõ để AI làm đúng chưa?

Trước một task kỹ thuật, ít nhất cần trả lời được năm câu:

1. Mục tiêu sản phẩm thật sự là gì?
2. Ràng buộc kỹ thuật là gì?
3. AI được phép sửa phạm vi nào?
4. Kết quả đúng được đo bằng gì?
5. Ai review và chịu trách nhiệm cuối cùng?

Nếu năm câu này chưa rõ, AI càng mạnh thì rủi ro càng lớn.

## Đặc tả đúng: kỹ năng bị xem nhẹ nhưng sẽ ngày càng đắt giá

Trong môi trường R&D, chúng ta hay muốn bắt tay vào làm nhanh. Có task là mở IDE. Có bug là nhảy vào code. Có yêu cầu mới là nghĩ ngay tới API, database, UI, driver.

Nhưng trong thời AI Agent, đặc tả kém là nguồn gốc của rất nhiều lãng phí.

Một yêu cầu như “làm tính năng điều khiển thiết bị” gần như chưa đủ để thực thi an toàn. Nó thiếu mục tiêu, thiếu đầu vào, thiếu đầu ra, thiếu điều kiện lỗi, thiếu ràng buộc, thiếu tiêu chí hoàn thành.

Đặc tả tốt không cần phải dài như tài liệu đấu thầu. Nhưng nó phải làm rõ những điều khiến hệ thống có thể đúng hoặc sai:

- Người dùng thật sự cần kết quả nào?
- Luồng chính là gì?
- Luồng lỗi là gì?
- Dữ liệu nào là nguồn sự thật?
- Điều gì tuyệt đối không được xảy ra?
- Có ảnh hưởng tới hệ thống cũ không?
- Có rủi ro bảo mật, hiệu năng, tài nguyên, tương thích không?
- Thế nào thì được coi là xong?

Khi đặc tả rõ, AI Agent trở thành lực lượng tăng tốc. Khi đặc tả mơ hồ, AI Agent trở thành máy nhân bản sự mơ hồ.

Đây là thay đổi lớn với cả Software Engineer, Firmware Engineer, Tester, BA, PM và Leader. Trong thời AI-native, viết yêu cầu rõ không còn là việc “mềm”. Nó là năng lực kỹ thuật.

## Kiến trúc đúng: AI có thể viết một hàm tốt, nhưng sản phẩm không được tạo ra từ một hàm tốt

Một hàm tốt chưa chắc tạo ra một hệ thống tốt. Một service chạy được chưa chắc phù hợp với kiến trúc. Một driver mẫu compile được chưa chắc an toàn trên phần cứng thật.

Sản phẩm tốt cần module rõ, boundary rõ, interface rõ, data flow rõ, state rõ, error flow rõ, ownership rõ, log rõ.

Đây là nơi vai trò của nhân sự R&D trở nên quan trọng hơn, không phải ít đi.

AI có thể đề xuất nhiều cách làm. Nhưng con người phải chọn cách phù hợp với hệ thống hiện tại, năng lực team hiện tại, rủi ro vận hành, khả năng maintain và lộ trình sản phẩm.

Với software, điều đó có thể là thiết kế API đủ rõ để AI và con người không dùng sai. Ví dụ `control_device(name, value)` rất tiện nhưng quá mơ hồ. Trong hệ thống có nhiều thiết bị, nhiều trạng thái, nhiều quyền, tool như vậy dễ gây lỗi. Những API như `set_device_power(device_id, power_state)`, `set_light_brightness(device_id, brightness_percent)`, `get_device_current_state(device_id)` rõ hơn vì chúng giảm nhập nhằng.

Với firmware, yêu cầu còn khắt khe hơn. Firmware không chỉ là code. Nó chạm vào điện áp, dòng điện, relay, motor, nhiệt độ, pin, sóng không dây, bus truyền thông, watchdog, flash, RAM, timing. AI có thể sinh driver mẫu, nhưng AI không đứng cạnh thiết bị thật để nghe relay đóng, đo dòng, nhìn oscilloscope, hay quan sát lỗi chỉ xảy ra sau 12 giờ chạy liên tục.

Firmware Engineer dùng AI tốt không phải là người copy code AI vào MCU. Đó là người biết yêu cầu:

> Hãy sinh state machine cho luồng này, không dùng dynamic allocation, RAM không vượt quá giới hạn, có timeout, có watchdog recovery, có retry policy, có log nhẹ, và có test mô phỏng mất gói truyền thông.

Đó là sự khác biệt giữa dùng AI như một công cụ viết code và dùng AI như một lực lượng thực thi trong một hệ thống được thiết kế.

## Kiểm chứng đúng: câu hỏi quan trọng nhất là “bằng chứng đâu?”

Sau khi AI tạo ra một kết quả, phản xạ đầu tiên không nên là “nhìn ổn không?”.

Phản xạ đúng hơn là:

> Bằng chứng nào cho thấy nó đúng?

Với software, bằng chứng có thể là unit test, integration test, contract test, E2E test, load test, security test, regression test. Với firmware, bằng chứng có thể là timing test, memory test, power test, long-run test, watchdog test, hardware-in-the-loop test, fault injection test.

Nếu không có kiểm chứng, AI tạo ra cảm giác tiến bộ. Nhưng cảm giác không đủ để release.

Một pull request do AI sinh ra có thể rất đẹp: đặt tên tốt, format sạch, comment hợp lý, test có vẻ đầy đủ. Nhưng vẫn có thể sai yêu cầu, sai kiến trúc, bỏ sót case lỗi, thêm coupling, hoặc làm hệ thống khó maintain hơn.

Vì vậy, năng lực review trong thời AI Agent sẽ trở nên quan trọng hơn. Review không chỉ là đọc code. Review là đối chiếu với đặc tả, kiến trúc, ràng buộc, test, log và rủi ro.

Một reviewer tốt sẽ hỏi:

- Có đúng yêu cầu không?
- Có phá kiến trúc hiện tại không?
- Có thêm coupling không cần thiết không?
- Có xử lý lỗi không?
- Có test case chính và case biên không?
- Có log đủ để debug không?
- Có rủi ro bảo mật, hiệu năng, tài nguyên không?
- Có làm hệ thống khó maintain hơn không?

AI có thể tạo ra nhiều code hơn. Nếu review yếu, lỗi cũng đi vào hệ thống nhanh hơn.

## Mindset mới: từ làm task sang thiết kế vòng lặp tạo giá trị

Tư duy cũ là: tôi nhận task và code cho xong.

Tư duy mới là: tôi làm rõ mục tiêu, thiết kế cách làm, đặt tiêu chí kiểm chứng, rồi dùng cả AI lẫn con người để thực thi an toàn.

Tư duy cũ là: code chạy được là xong.

Tư duy mới là: code đúng yêu cầu, đúng kiến trúc, có test, có log, có bằng chứng, và không làm hệ thống xấu đi mới là xong.

Tư duy cũ là: AI là công cụ phụ.

Tư duy mới là: AI là lực lượng thực thi cần được quản trị bằng scope, context, tool, test, approval và review.

Một nhân sự AI-native không chỉ hỏi “tôi phải làm gì?”. Người đó hỏi:

> Làm sao để lần sau team làm việc này nhanh hơn, an toàn hơn, ít lỗi hơn?

Đây là sự khác biệt giữa hoàn thành một task và nâng cấp năng lực của cả team.

![Đội R&D cùng thiết kế hệ thống AI-native có kiểm chứng](assets/rd-team-ai-native.png)

## Một mô hình dễ nhớ: 5Đ

Để chuyển tư duy thành hành động, phòng R&D có thể dùng mô hình 5Đ trước mỗi task quan trọng:

**Đúng vấn đề**: có đang giải đúng pain point không, hay chỉ đang làm theo một yêu cầu chưa được làm rõ?

**Đúng thiết kế**: module, interface, state, error flow, ownership có hợp lý không?

**Đúng dữ liệu**: input, output, source of truth, trạng thái xác nhận có rõ không?

**Đúng điều kiện lỗi**: offline, timeout, packet loss, trùng tên, thiếu quyền, brown-out, retry, rollback đã được tính chưa?

**Đúng kiểm chứng**: có test, log, benchmark, hardware evidence hoặc tiêu chí đo để chứng minh không?

Chỉ khi đủ 5Đ, chúng ta mới nên tin rằng task thật sự xong.

## Thói quen mới: viết Definition of Done trước khi code

Một thay đổi nhỏ nhưng tác động lớn là viết Definition of Done trước khi bắt đầu.

Ví dụ:

```markdown
Task được coi là hoàn thành khi:

1. User có thể bật/tắt thiết bị theo phòng.
2. Nếu thiết bị offline, hệ thống không báo thành công giả.
3. Nếu có nhiều thiết bị phù hợp, hệ thống hỏi lại hoặc xử lý theo rule đã định.
4. Có test cho happy path, offline, timeout, nhiều thiết bị, thiếu quyền.
5. Có log trace từ user command tới tool call và phản hồi thiết bị.
6. Không thay đổi public API hiện tại.
7. Không làm tăng latency trung bình quá 10%.
```

Khi Definition of Done rõ, AI làm việc tốt hơn, reviewer dễ hơn, tester rõ hơn, PM theo dõi dễ hơn, leader đánh giá rủi ro tốt hơn.

Đây không phải là thêm thủ tục. Đây là giảm chi phí mơ hồ.

## AI sẽ thay thế ai?

Câu hỏi này cần trả lời thẳng.

AI Agent dễ thay thế những người chỉ làm theo hướng dẫn mơ hồ, không hiểu hệ thống, không kiểm chứng kết quả, không nâng cấp cách làm.

Nhưng AI sẽ khuếch đại rất mạnh những người hiểu bản chất bài toán, biết chia hệ thống, biết viết đặc tả, biết review, biết test, biết đo lường, biết thiết kế tool và quy trình, biết chịu trách nhiệm với chất lượng cuối cùng.

Khoảng cách không nằm ở việc ai dùng AI nhiều hơn. Khoảng cách nằm ở việc ai dùng AI với tư duy hệ thống tốt hơn.

Người chỉ hỏi AI “viết giúp tôi code” sẽ nhận được code.

Người biết đưa cho AI mục tiêu, bối cảnh, ràng buộc, scope, tiêu chí done, test bắt buộc và cách review sẽ nhận được một vòng lặp thực thi tốt hơn.

## Ba mươi ngày để bắt đầu thay đổi

Tuần đầu tiên, hãy tập viết task rõ hơn. Mỗi task cần có mục tiêu, scope, constraint, Definition of Done và test case chính. Không cần hoàn hảo, nhưng phải rõ hơn hôm qua.

Tuần thứ hai, hãy dùng AI có kiểm soát. Giao AI đọc code, tạo test, refactor nhỏ, viết tài liệu, tìm rủi ro. Nhưng luôn giới hạn phạm vi và review lại.

Tuần thứ ba, hãy tập thiết kế test và log. Mỗi task cần trả lời: test gì để chứng minh đúng, log gì để debug khi sai, metric gì để biết tốt hơn.

Tuần thứ tư, hãy dùng AI để nâng cấp quy trình team. Tạo checklist review, template task, test plan, tài liệu onboarding, bộ câu hỏi phân tích lỗi, bản tóm tắt bug pattern. Mục tiêu không chỉ là cá nhân làm nhanh hơn, mà là cả team trưởng thành hơn.

## Kết lại

Thời AI Agent không làm nhân sự R&D bớt quan trọng. Nó làm vai trò của chúng ta thay đổi.

Trước đây, người giỏi là người tự làm đúng.

Bây giờ, người giỏi là người làm cho con người, AI, tool, test, log và hệ thống cùng làm đúng.

Giá trị dịch chuyển từ viết code sang hiểu đúng vấn đề, đặc tả đúng yêu cầu, thiết kế đúng kiến trúc, giao việc đúng cho AI, kiểm chứng đúng kết quả và chịu trách nhiệm đúng với chất lượng sản phẩm.

Nếu phải chọn một nền tảng tư duy quan trọng nhất, đó là:

> Tư duy hệ thống có kiểm chứng.

Vì trong thời AI Agent, làm nhanh không còn đủ. Phải làm đúng.

Làm đúng cũng chưa đủ. Phải chứng minh được là đúng.

Và chứng minh đúng vẫn chưa đủ. Phải biến nó thành quy trình để cả team cùng làm đúng nhanh hơn.

Trước mỗi task, mỗi người trong phòng R&D có thể tự hỏi một câu:

> Tôi đang chỉ làm cho xong task, hay đang thiết kế một cách làm giúp cả hệ thống và cả team tốt hơn?

Nếu câu hỏi này xuất hiện thường xuyên hơn trong các cuộc trao đổi kỹ thuật, AI Agent sẽ không còn là mối đe dọa. Nó sẽ trở thành một lực lượng thực thi mạnh, với điều kiện chúng ta đủ rõ ràng, đủ kỷ luật và đủ năng lực để dẫn dắt nó.

