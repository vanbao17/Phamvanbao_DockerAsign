import classNames from "classnames/bind";
import styles from "./SideBar.module.scss";
const cx = classNames.bind(styles);

function SideBar() {
  return (
    <div className={cx("wrapper")}>
      <div className={cx("container-logo")}>
        <span className={cx("name")}>PVB</span>
      </div>
      <div className={cx("container-cate")}>
        <span>Danh mục sản phẩm</span>
      </div>
    </div>
  );
}

export default SideBar;
