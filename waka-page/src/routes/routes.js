import configs from "../configs/configs";
import Home from "../layout/Home/Home";
import Search from "../layout/Search/Search";

const publicRoutes = [
  {
    path: configs.home,
    component: Home,
  },
  {
    path: configs.search,
    component: Search,
  },
];
export default publicRoutes;
