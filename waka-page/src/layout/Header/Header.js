import classNames from "classnames/bind";
import styles from "./Header.module.scss";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSearch, faUser } from "@fortawesome/free-solid-svg-icons";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
const cx = classNames.bind(styles);
function Header() {
  const nav = useNavigate();
  const [dataInput, setDataInput] = useState("");
  const [dataSearch, setdataSearch] = useState([]);
  const handleInput = (e) => {
    setDataInput(e.target.value);
  };
  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      nav(`/search`, { state: { dt: dataSearch } });
    }
  };
  const url = "/search";
  useEffect(() => {
    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query: dataInput }),
    };
    if (dataInput != "") {
      fetch(url, options)
        .then((response) => response.json())
        .then((dt) => {
          if (dt.error) {
            setdataSearch([]);
          } else {
            setdataSearch(dt.data);
          }
          console.log(dt);
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
        });
    } else {
      setdataSearch([]);
    }
  }, [dataInput]);
  return (
    <div className={cx("wrapper")}>
      <span>Trang chủ</span>
      <div className={cx("container-input")}>
        <input
          onChange={handleInput}
          onKeyDown={handleKeyDown}
          type="text"
          placeholder="Tìm kiếm sản phẩm"
        ></input>
        <FontAwesomeIcon
          className={cx("icon", "icon-search")}
          icon={faSearch}
        />
        {dataSearch.length != 0 ? (
          <>
            <div className={cx("dropbox-search")}>
              <ul className={cx("list-search")}>
                {dataSearch != undefined ? (
                  dataSearch.map((book, index) => {
                    return <li key={index}>{book[1]}</li>;
                  })
                ) : (
                  <></>
                )}
              </ul>
            </div>
          </>
        ) : (
          <></>
        )}
      </div>
      <div className={cx("container-user")}>
        <FontAwesomeIcon icon={faUser} className={cx("icon", "icon-user")} />
      </div>
    </div>
  );
}

export default Header;
