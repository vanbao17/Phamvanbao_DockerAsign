import BookItem from "../../components/BookItem/BookItem";
import classNames from "classnames/bind";
import styles from "./Search.module.scss";
import { useState } from "react";
import { useLocation } from "react-router-dom";
const cx = classNames.bind(styles);
function Search() {
  const location = useLocation();
  const data = location.state?.dt;
  const [dataBooks, setdataBooks] = useState([]);
  useState(() => {
    if (data != undefined) {
      setdataBooks(data);
    }
  }, [data]);
  return (
    <div className={cx("wrapper")}>
      <div className={cx("container")}>
        <h3>Danh sách tìm kiếm</h3>
        <div className={cx("list-books")}>
          {dataBooks.length === 0 ? (
            <>Không có sách mà bạn muốn tìm</>
          ) : (
            <>
              {dataBooks != undefined ? (
                dataBooks.map((book, index) => {
                  return <BookItem key={index} data={book} />;
                })
              ) : (
                <></>
              )}
            </>
          )}
        </div>
      </div>
    </div>
  );
}

export default Search;
