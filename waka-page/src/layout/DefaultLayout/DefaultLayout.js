import classNames from "classnames/bind";
import styles from "./DefaultLayout.module.scss";
import SideBar from "../SideBar/SideBar";
import Header from "../Header/Header";
import Home from "../Home/Home";
const cx = classNames.bind(styles);

function DefaultLayout({ children }) {
  return (
    <div className={cx("wrapper")}>
      <div className={cx("wrapper-left")}>
        <SideBar />
      </div>
      <div className={cx("wrapper-right")}>
        <Header />
        {children}
      </div>
    </div>
  );
}

export default DefaultLayout;
