import { Fragment } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import publicRoutes from "./routes/routes";
import DefaultLayout from "./layout/DefaultLayout/DefaultLayout";
function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          {publicRoutes.map((item, index) => {
            let Layout = DefaultLayout;
            if (item.layout) {
              Layout = item.layout;
            } else {
              if (item.layout === null) {
                Layout = Fragment;
              }
            }
            const Page = item.component;
            return (
              <Route key={index}>
                <Route
                  key={index}
                  path={item.path}
                  element={
                    <Layout>
                      <Page data={item.path}></Page>
                    </Layout>
                  }
                ></Route>
              </Route>
            );
          })}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
