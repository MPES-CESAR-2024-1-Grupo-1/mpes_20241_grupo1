/* eslint-disable prettier/prettier */
// eslint-disable-next-line import/order
"use client";
import { Button } from "@nextui-org/button";

import { Input } from "@nextui-org/input";
import { handleSubmit } from '@/actions/form_submit'
import { useState } from "react";


export default function FormTeste() {


   const [gptReposta, setGptReposta] = useState("RESPOSTA INICIAL");

    async function myHandler(data: FormData){
        let retorno = await handleSubmit(data);

        if(retorno !== undefined){
            setGptReposta(retorno);
        }
    }


    return (
        <div className="
            h-screen  
            flex flex-col 
            // flex-grow 
            gap-2
            ">

            <h1>URL DA API É: {process.env.URL_BE}</h1>

        <div className="h-[800] min-h-[800] w-[700] overflow-y-scroll border border-gray-300 p-4">



<div 
    className="h-[800] min-h-[800] w-[700]"
    dangerouslySetInnerHTML={{ __html: gptReposta }} 
    />

        </div>
            <form
                action={ myHandler} 
                method="POST"
                className="
                    container flex flex-col gap-4 justify-end "
            >

                <Input 
                    name="pergunta" 
                    type="text" 
                    label="PERGUNTA"
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








