// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract AntiquesMarket
{
    struct Item //The antiques objects
    {
        uint id;
        string name;
        uint cost;
        address owner;
    }

    Item [] items;

    struct Sale //The sales antiques objects
    {
        uint id;
        address saller;
        address buyer;
        uint idItem;
        uint cost;
        bool status;
    }

    Sale [] sales;

    function createItem (string memory name, uint cost) public
    {
        items.push(items.length, name, cost, msg.sender);
    }

    address NullAddress = 0x0000000000000000000000000000000000000000;

    function saleItem (uint idItem, uint _cost) public
    {
        require (msg.sender == items[idItem].owner, "You don't have this item");
        sales.push(Sale(sales.length, msg.sender, NullAddress, idItem, _cost, false));
    }

    function checkItem (uint id) public view returns (Item)
    {
        require (id < items.length, "error");
        return (items[id].id, items[id].name, items[id].cost, items[id].owner);
    }

    function checkSale () public view returns (Sale [] memory)
    {
        return (sales);
    }

    function confirmSale (uint idSale) public payable
    {
        require (sales[idSale].saller != msg.sender, "You have this item");
        require (sales[idSale].status == false, "Just sold");
        require (msg.value >= sales[idSale].cost, "Insufficient funds");
        transfer(sales[idSale].saller).transfer(sales[idSale].cost);
        sales[idSale].status = true;
        sales[idSale].buyer = msg.sender;
        items[sales[idSale].idItem].owner = msg.sender;
    }
}