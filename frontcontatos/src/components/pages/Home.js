import styles from "./Home.module.css";
import Input from "../layout/Input";
import SubmitButton from "../layout/SubmitButton";
import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { LocalStorage } from 'ttl-localstorage';
export default function Home(props) {
  //   const { code } = useParams();
  const [contato, setContato] = useState([]);
  // LocalStorage.put('myKey', 'data', 20);

  let navigate = useNavigate();
  //   const location = useLocation()
  // const x = new URL(location.href).searchParams.get('code')
  // console.log(x)
  let code = (window.location.search.split('='))
  //   const search = props.location.search;
  //   const name = new URLSearchParams(search).get('code');

  useEffect(() => {
    // console.log("to aqui " + localStorage.getItem("access-token"));
    // console.log('12312 ' + LocalStorage.get('access-token'))
    // console.log('1231212321312321 ' + LocalStorage.get('refresh-token'))
    // // var init;
    if (!LocalStorage.get('access-token')){
      const init = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ "code": code[1] })
      }
      fetch("http://localhost:8000/api/auth/token/", init)
      // fetch("http://localhost:8000/api/auth/token/", init)
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          LocalStorage.put('access-token', data.access_token, 1800);
          LocalStorage.put('refresh-token', data.refresh_token);
          // localStorage.setItem("access-token", data.access_token);
          navigate('/')
        })
        .catch((error) => console.log(error))
    }else{
      const init = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ "refresh_token": LocalStorage.get('refresh-token') })
      }
      fetch("http://localhost:8000/api/auth/token/", init)
      // fetch("http://localhost:8000/api/auth/token/", init)
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          LocalStorage.put('access-token', data.access_token, 1800);
          LocalStorage.put('refresh-token', data.refresh_token);
          // localStorage.setItem("access-token", data.access_token);
          navigate('/')
        })
        .catch((error) => console.log(error))
    }
  }, []);
  // if (localStorage.getItem) {

  const cadastrarContato = (e) => {
    e.preventDefault();
    const init = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ "data": { "properties": contato }, "access_token": LocalStorage.get('access-token') }),
    };
    fetch("http://localhost:8000/contatos/create/", init)
      .then()
      .then()
      .catch((error) => console.log(error));
  };
  function handleTeste(e) {
    e.preventDefault();
    const init = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ "access_token": localStorage.getItem("access-token") }),
    };
    fetch("http://localhost:8000/contatos/", init)
      .then()
      .then()
      .catch((error) => console.log(error));
  }
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
            name="date_of_birth"
            type="date"
            handleOnChange={handleChange}
          />
          <Input
            text="Peso"
            name="weight"
            placholder="Peso (kg)"
            type="text"
            handleOnChange={handleChange}
          />
          <SubmitButton text="Criar contato" />
          <button type="button" onClick={handleTeste}>listar</button>
        </form>
      </div>
    </div>
  );
}
