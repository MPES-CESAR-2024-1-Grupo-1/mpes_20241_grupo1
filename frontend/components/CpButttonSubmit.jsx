/* eslint-disable import/order */
/* eslint-disable prettier/prettier */
// eslint-disable-next-line import/order
"use client";
import { Button } from "@nextui-org/button";
import { useFormStatus } from "react-dom";



export default function CpButtonSubmit() {

    const {pending} = useFormStatus();


    console.log(`esta pendente: ${pending}`);

    return (
        <Button
            type="submit" 
            color="primary" 
            variant="solid"
            disabled={pending}
            isLoading={pending}
            fullWidth={true}
            radius="none"
            size="md"
            className="w-[700] mb-28"
        >
            {  pending ? "Carregando..." : "Enviar" }
        </Button>
    );
}








