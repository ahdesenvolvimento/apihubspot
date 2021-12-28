import styles from "./Home.module.css";
import Input from "../layout/Input";
import SubmitButton from "../layout/SubmitButton";
import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
export default function Home(props) {
  //   const { code } = useParams();
  const [contato, setContato] = useState([]);
//   const location = useLocation()
// const x = new URL(location.href).searchParams.get('code')
// console.log(x)
  console.log(window.location.search.split('='))
  //   const search = props.location.search;
  //   const name = new URLSearchParams(search).get('code');

  useEffect(() => {
    console.log(localStorage.getItem("access-token"));
    // const init = {
    //   method: "GET",
    //   headers: {
    //     "Content-Type": "application/json",
    //   },
    // };
    // fetch("http://localhost:8000/", init)
    //   .then((response) => response.json())
    //   .then((data) => {
    //     console.log(data);
    //     localStorage.setItem("access-token", data.access_token);
    //   })
    //   .catch((error) => console.log(error));
  }, []);
  // if (localStorage.getItem) {

  const cadastrarContato = (e) => {
    e.preventDefault();
    const init = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(contato),
    };
    fetch("http://localhost:8000/contatos/", init)
      .then()
      .then()
      .catch((error) => console.log(error));
  };

  const handleChange = (e) => {
    setContato({ ...contato, [e.target.name]: e.target.value });
  };
  return (
    <div className={styles.content}>
      <div className={styles.form}>
        <form method="POST" action="" onSubmit={cadastrarContato}>
          <Input
            text="E-mail"
            name="email"
            placholder="Insira o e-mail do contato"
            type="email"
            handleOnChange={handleChange}
          />
          <Input
            text="Telefone"
            name="phone"
            placholder="Telefone"
            type="text"
            handleOnChange={handleChange}
          />
          <Input
            text="Data do aniversário"
            name="birthday"
            type="date"
            handleOnChange={handleChange}
          />
          <Input
            text="Peso"
            name="peso"
            placholder="Peso (kg)"
            type="text"
            handleOnChange={handleChange}
          />
          <SubmitButton text="Criar contato" />
        </form>
      </div>
    </div>
  );
}
