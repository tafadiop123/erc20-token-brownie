// contracts/OurToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

//On va construire un token qui traque l'or (GLD), une monnaie interne dans un jeu hypothétique.
contract OurToken is ERC20 {
    //Dans le constructeur on va mettre une Offre initial (initialSupply) qui sera en Wei
    //Puis on va mettre le nom de notre actif et son symbole dans les parametres
    constructor(uint256 initialSupply) ERC20("OurToken", "OT") {
        _mint(msg.sender, initialSupply);
    }
}
