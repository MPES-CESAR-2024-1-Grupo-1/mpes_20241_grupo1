/* eslint-disable import/order */
/* eslint-disable prettier/prettier */
// eslint-disable-next-line import/order
"use client";
import { Button } from "@nextui-org/button";

import CpButtonSubmit from "@/components/CpButttonSubmit";

import { Input } from "@nextui-org/input";
import { handleSubmit } from '@/actions/form_submit'
import { useState } from "react";
import { useFormStatus } from "react-dom";




export default function FormTeste() {


    const [gptReposta, setGptReposta] = useState("");
    const {pending} = useFormStatus();


    async function myHandler(data: FormData){
        let retorno = await handleSubmit(data);

        if(retorno !== undefined){
            setGptReposta(retorno);
        }
    }

    // className="h-[400] min-h-[400] w-[700]"
    // dangerouslySetInnerHTML={{ __html: gptReposta }} 


    return (
        <div className="
            h-screen  
            flex flex-col 
            // flex-grow 
            gap-2"
        >

            <div 
                className="
                h-[400] 
                min-h-[400] 
                w-[700] 
                overflow-y-scroll border 
                border-gray-300 p-4"
            >
                <span dangerouslySetInnerHTML={{ __html: gptReposta }} />
            <div/>

        <div/>

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
                    label="Pergunte sobre algo de História. ==> Aqui < ==="
                    className="w-[700]"
                />

                <CpButtonSubmit />
            </form>
        </div>  
        
    );
}








