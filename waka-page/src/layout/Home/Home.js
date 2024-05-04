import classNames from "classnames/bind";
import styles from "./Home.module.scss";
import BookItem from "../../components/BookItem/BookItem";
import { useEffect, useState } from "react";
const cx = classNames.bind(styles);
function Home() {
  const [books, setBooks] = useState([]);
  const url = "/books";
  useEffect(() => {
    fetch(url)
      .then((response) => response.json())
      .then((dt) => setBooks(dt.data))
      .catch((err) => console.error("Không thể kết nối tới API server", err));
  }, []);

  return (
    <div className={cx("wrapper")}>
      <div className={cx("container")}>
        <h3>Danh sách truyện</h3>
        <div className={cx("list-books")}>
          {books.length === 0 ? (
            <>Fetch dữ liệu chưa thằng chóa</>
          ) : (
            <>
              {books.map((book, index) => {
                return <BookItem key={index} data={book} />;
              })}
            </>
          )}
        </div>
      </div>
    </div>
  );
}

export default Home;
