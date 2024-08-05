/* eslint-disable prettier/prettier */
"use client";
import { Button } from "@nextui-org/button";
import { Tooltip } from "@nextui-org/tooltip";
import { Accordion, AccordionItem } from "@nextui-org/accordion";
import Link from "next/link";
import { Divider } from "@nextui-org/divider";
import {
    FcBullish,
    FcHome,
    FcSupport,
    FcCalculator,
    FcDataSheet,
    FcGraduationCap,
    FcBusinessman,
} from "react-icons/fc";


// import { NavButton } from "@/src/ui/nav_button";

export default function CpMenuLateral() {

    return (
    <div>
    
        {/* HOME */}
        <Link href={"/"}>
            <Button
            fullWidth
            className="text-base font-bold"
            color="primary"
            css={{ paddingLeft: "0px" }}
            variant="light"
            >
            Home
            </Button>
        </Link> {/* HOME END */}

        <Divider />

        <Accordion showDivider={false}>

            {/* DASHBOAD */}
            <AccordionItem
            key="2"
            aria-label="Accordion 2"
            startContent={<FcBullish />}
            title="Dashboad"
            >
            <Link href={"/"}>
                <Button
                className="justify-start text-base"
                color="primary"
                startContent={<FcBullish />}
                variant="light"
                >
                Painel 01
                </Button>
            </Link>

            <Link href={"/"}>
                <Button
                fullWidth
                className="justify-start text-base"
                color="primary"
                startContent={<FcBullish />}
                variant="light"
                >
                Painel 02
                </Button>
            </Link>
            </AccordionItem>

            

            {/* ADMINISTRAÇÃO */}
            <AccordionItem
            key="3"
            aria-label="Accordion 3"
            startContent={<FcBusinessman />}
            title="Administração"
            >
                <Link href={"/teste"}>
                    <Tooltip
                    content="Gerencia Usuários [NÃO IMPLEMENTADO]."
                    placement="right-end"
                    >
                    <Button
                        fullWidth
                        className="justify-start text-base"
                        color="primary"
                        startContent={<FcSupport />}
                        variant="light"
                    >
                        Gerencia Usuários
                    </Button>
                    </Tooltip>
                </Link>

            </AccordionItem>

        </Accordion>

    </div>
  );
}
