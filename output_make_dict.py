def make_dictionary_original(make_product_information_dict):
    make_product_information_dict_result = {}
    make_product_information_dict_comparison = [
        "품명|영어",
        "범주",
        "브랜드/품번",
        "인기도(1개월_장바구니)",
        "누적판매",
        "좋아요",
        "구매후기",
        "배송방법",
        "평균배송일",
        "판매가",
        "세일가",
        "링크",
    ]
    make_product_information_dict_key_list = list(make_product_information_dict.keys())
    for num in range(len(make_product_information_dict_comparison)):
        if (
            make_product_information_dict_comparison[num]
            in make_product_information_dict_key_list
        ):
            make_product_information_dict_result.update(
                {
                    make_product_information_dict_comparison[
                        num
                    ]: make_product_information_dict[
                        make_product_information_dict_comparison[num]
                    ]
                }
            )
        else:
            make_product_information_dict_result.update(
                {make_product_information_dict_comparison[num]: ""}
            )
    return make_product_information_dict_result
