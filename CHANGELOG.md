# Changelog

Tất cả thay đổi đáng chú ý của dự án được ghi lại trong tệp này.
Dự án tuân theo [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Thêm `Cart.sort_by_title()` và `Cart.sort_by_cost()` để sắp xếp giỏ hàng.

## [1.0.0] - 2026-11-03

### Added

- Thêm `Cart.print_cart()` để hiển thị nội dung giỏ hàng.
- Thêm `search_by_title()` để tìm DVD theo tiêu đề.
- Thêm `total_cost_with_discount()` để tính tổng tiền sau giảm giá.
- Thêm kiểm thử tự động cho giỏ hàng, tìm kiếm và giảm giá.

### Fixed

- Không cho phép thêm DVD thứ 21 vào giỏ hàng (#6).

[Unreleased]: https://github.com/dangtandat-tech/IT3080_Lab/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/dangtandat-tech/IT3080_Lab/releases/tag/v1.0.0
