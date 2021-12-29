// import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { Link, BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/pages/Home";
import Login from "./components/pages/Login";
import { Container } from "react-bootstrap";
import"./App.css";

function App() {
  return (
    <div className="">
      <Container>
        <Router>
          <div className="content">
            <div className="form">
              <Routes>
                <Route exact path="/" element={<Home />} />
                <Route path="/login" element={<Login />} />
              </Routes>
            </div>
          </div>
        </Router>
      </Container>
    </div>
  );
}

export default App;
