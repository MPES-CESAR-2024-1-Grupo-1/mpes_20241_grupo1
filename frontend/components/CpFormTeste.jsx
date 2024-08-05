/* eslint-disable prettier/prettier */
'use client'
import { Button } from "@nextui-org/button";
import {Card, CardHeader, CardBody, CardFooter} from "@nextui-org/card";
import Divider from "@nextui-org/divider";
import Link  from "@nextui-org/link";
// import {
//     Card, 
//     CardHeader, 
//     CardBody, 
//     CardFooter, 
//     Divider, 
//     Link, 
//     Image
// } from "@nextui-org/react";



import { Input } from "@nextui-org/input";
import { useState } from "react";


export default function CpFormTeste() {

    const [formulario, setFormulario] = useState({
        user_id : "",
        conversar_id : "",
        pergunta : ""
    });

    const [gptReposta, setGptReposta] = useState("RESPOSTA INICIAL");

// const res = await fetch('http://localhost:5000/form_teste', {

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        
        const res = await fetch('http://localhost/api/form_teste', {
            method: 'POST',
            headers: {
                "Access-Control-Allow-Origin" : "*",
                "Content-Type": "application/json",
                "Access-Control-Allow-Methods" : "GET,POST,PUT,DELETE,OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
            },
            body: JSON.stringify(formulario)
        });
    
        if (res.ok) {
            const textoResposta = await res.text();
          // Lógica para quando o envio for bem-sucedido
            console.log('Formulário enviado com sucesso!');
            console.log( textoResposta );
            setGptReposta( textoResposta )
        } else {
          // Lógica para quando houver um erro
            console.error('Erro ao enviar o formulário');
        }
    };




    const handleChangeValues = (v) =>{
        let inpup_name = v.target.name;
        let input_value = v.target.value;

        setFormulario({
            ...formulario, [inpup_name]: input_value 
        });

        console.log(formulario);
    };

    
    return (
        <div className="
            h-screen  
            flex flex-col 
            // flex-grow 
            gap-2
            ">


        <div className="h-[800] min-h-[800] w-[700] overflow-y-scroll border border-gray-300 p-4">



<div 
    className="h-[800] min-h-[800] w-[700]"
    dangerouslySetInnerHTML={{ __html: gptReposta }} />

        </div>


            <form 
                onSubmit={handleSubmit}
                className="
                    container flex flex-col gap-4 justify-end "
            >

                <Input 
                    name="pergunta" 
                    type="text" 
                    label="PERGUNTA"
                    value={formulario.pergunta}
                    onChange={handleChangeValues} 
                    className="w-[700]"
                />
                
                <Button
                    type="submit" 
                    color="primary" 
                    variant="solid"
                    className="w-[300] h-9 mb-28"
                >
                    Submit
                </Button>

            </form>
        </div>  
        
    );
}










//   const handleSubmit = async (e) =>{
//     const URL_TESTE = "http://localhost:5000/form_teste"

//     // Evita o submit do form
//     e.preventDefault();   
//     // Pega o form
//     let meu_form = e.currentTarget;

//     // headers: {
//     //     "Access-Control-Allow-Origin" : "no-cors"
//     // },

//     meu_form_data = new FormData(meu_form);
//     console.log( Object.fromEntries(meu_form_data));

//     const res = await fetch('http://localhost:5000/form_teste', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(formulario)
//       });
  
//       if (res.ok) {
//         // Lógica para quando o envio for bem-sucedido
//         console.log('Formulário enviado com sucesso!');
//       } else {
//         // Lógica para quando houver um erro
//         console.error('Erro ao enviar o formulário');
//       }


// }

