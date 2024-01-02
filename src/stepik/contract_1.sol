// SPDX-License-Identifier: MIT
pragma solidity <=0.9.0;
contract Renta {
    address owner;
    uint code;
    uint cost;
    bool status = false;

    modifier CheckOwner() {
        require (msg.sender != owner, "You are the owner");
        _;
    }

    modifier CheckCode(uint _code) {
        require (_code/1000 > 0 && _code/1000<10, "Invalide code");
        _;
    }

    function CreateRenta(uint _code, uint _cost) public CheckCode(_code) {
        owner = msg.sender;
        code = _code;
        cost = _cost*10^18;
    }

    function ConfirmRenta(uint _code) public payable CheckCode(_code) CheckOwner {
        if ((_code == code) && (msg.value == cost)) {
            payable(owner).transfer(msg.value);
            status = true;
        }
        else {
            payable(msg.sender).transfer(msg.value);
        }
    }

    function CancelRent() public {
        require(!status, "The deal is already confirmed");
        require(msg.sender == owner, "Only the owner can cancel the rent");

        code = 0;
    }
}