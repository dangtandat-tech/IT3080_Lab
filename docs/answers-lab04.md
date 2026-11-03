# Trả lời thảo luận Lab 04

## Vì sao chuẩn bị trên master trước, không sửa trên nhánh release?

Nhánh `release/*` là baseline đã đóng băng để phát hành và bảo trì. Chuẩn bị
phiên bản trên `master` qua Pull Request giúp mã nguồn, số phiên bản và
CHANGELOG được review cùng nhau. Sau đó `release/lab04` chỉ việc trỏ đến
commit đã được kiểm tra.

## Vì sao release/* không merge ngược vào master?

`master` là dòng phát triển chính, còn `release/*` đại diện cho một dòng
bảo trì cụ thể. Merge toàn bộ release ngược lại dễ đưa theo các thay đổi
chỉ dành cho bản cũ. Nếu có hotfix cần dùng chung thì chuyển đúng commit
bằng `cherry-pick` và review riêng.

## So sánh Release Flow với GitFlow

Release Flow trong bài đơn giản hơn: `master` luôn là dòng phát triển và
nhánh release được giữ lại để bảo trì. GitFlow có thêm nhánh `develop`,
nhánh release tạm thời và quy tắc merge hai chiều phức tạp hơn.

## Vì sao lên 1.0.0 thay vì 0.4.0?

Các bản 0.x là giai đoạn phát triển ban đầu, API còn có thể thay đổi.
Bản 1.0.0 đánh dấu baseline đầu tiên ổn định và sẵn sàng phát hành;
từ đó các thay đổi tuân theo quy tắc MAJOR.MINOR.PATCH.
