import classNames from "classnames/bind";
import styles from "./BookItem.module.scss";
const cx = classNames.bind(styles);
function BookItem({ data }) {
  return (
    <div className={cx("book")}>
      <div className={cx("thumb")}>
        <img src={data[3]}></img>
      </div>
      <div className={cx("book-infor")}>
        <p className={cx("author")}>{data[2]}</p>
        <p className={cx("name")}>{data[1]}</p>
      </div>
    </div>
  );
}

export default BookItem;
