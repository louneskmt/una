import una
import asyncio

invoice = dict({
    "amount": 1000,
    "description": "test bindings"
})

async def lnd_rest():
    config_lnd_rest = dict({
        "url": "https://127.0.0.1:8081",
        "macaroon": "0201036c6e6402f801030a100249a596de122aa0b6cee0d446f166231201301a160a0761646472657373120472656164120577726974651a130a04696e666f120472656164120577726974651a170a08696e766f69636573120472656164120577726974651a210a086d616361726f6f6e120867656e6572617465120472656164120577726974651a160a076d657373616765120472656164120577726974651a170a086f6666636861696e120472656164120577726974651a160a076f6e636861696e120472656164120577726974651a140a057065657273120472656164120577726974651a180a067369676e6572120867656e657261746512047265616400000620a66d3da5b13d50b2c506a2191927bce8ef13e8fd192af2c69b5dcefddb97199d",
        "tls_certificate": "2d2d2d2d2d424547494e2043455254494649434154452d2d2d2d2d0a4d4949434a7a434341637967417749424167495141553567664541653374586471776a6c494b476f6e6a414b42676771686b6a4f50515144416a41784d5238770a485159445651514b45785a73626d5167595856306232646c626d56795958526c5a43426a5a584a304d51347744415944565151444577566862476c6a5a5441650a467730794d6a41344d5455784e544d334e444a61467730794d7a45774d5441784e544d334e444a614d444578487a416442674e5642416f54466d78755a4342680a645852765a3256755a584a686447566b49474e6c636e5178446a414d42674e5642414d544257467361574e6c4d466b77457759484b6f5a497a6a3043415159490a4b6f5a497a6a30444151634451674145796c494245585854544d6f76526f594c515064454c6a38626a7257656744637556564b3044744b4a78774d65773754440a342b6f4c754438334c546b697137446b2b6d6842505a6e782f4f4754474b7a754a4c314465364f4278544342776a414f42674e56485138424166384542414d430a41715177457759445652306c42417777436759494b775942425155484177457744775944565230544151482f42415577417745422f7a416442674e56485134450a4667515563616b6351494e38553048734c735752527544394d304f47306d6b77617759445652305242475177596f4946595778705932574343577876593246730a6147397a644949465957787059325743446e4276624746794c5734784c57467361574e6c67675231626d6c3467677031626d6c346347466a61325630676764690a64575a6a623235756877522f4141414268784141414141414141414141414141414141414141414268775373465141454d416f4743437147534d343942414d430a41306b414d45594349514364767236702f466446464866597871596279594b483635344e6e7372557779344f544648386c31727662514968414f5433546c437a0a77477863642b35416367364e31596472652b76544f2f34525371636c7a5a6532776151520a2d2d2d2d2d454e442043455254494649434154452d2d2d2d2d0a"
    })

    lnd_rest = una.Node("LndRest", config_lnd_rest)
    print(await lnd_rest.get_info())
    print(await lnd_rest.create_invoice(invoice))
    print(await lnd_rest.pay_invoice(dict({
        "payment_request": "lnbcrt10u1p306998pp53jzmkeummuu0u6rfxpcgx7rk5adturte8mppr64032nek3jmjtvqdq4w3jhxapqvf5kuerfdenhxcqzpgxqrrsssp53nhngg8858l2ch63ks3yc2uetzf4gnctp9xccqxuchztxmahd2as9qyyssqzl6m9rwgwp0r5a6de7fj98k42sn7vvf30n6k2ymcq7wvmk4689ls7zewqq9x5maqa60tshdmhu3gx3dd243vh9h9xralrfrjpfwfn3gq6xml7k"
    })))

async def cln_grpc():
    config_cln_grpc = dict({
        "url": "https://localhost:11002",
        "tls_certificate": "2d2d2d2d2d424547494e2043455254494649434154452d2d2d2d2d0d0a4d494942636a434341526967417749424167494a414d466c546169526559526a4d416f4743437147534d343942414d434d4259784644415342674e5642414d4d0d0a43324e73626942536232393049454e424d434158445463314d4445774d5441774d4441774d466f59447a51774f5459774d5441784d4441774d444177576a41570d0a4d52517745675944565151444441746a62473467556d3976644342445154425a4d424d4742797147534d34394167454743437147534d343941774548413049410d0a424c4344514c387469663542445051643943715976776361756749752b757274616e554359536c6b4b714b3736562f4d66646b307372464c364c6d6e684b32720d0a61434c494b475841334f4f545038426e5a5a3144547a4b6a5454424c4d426b4741315564455151534d42434341324e73626f494a6247396a5957786f62334e300d0a4d42304741315564446751574242526a68486d527145316c775a56656b53735a374f56456d4a6c65736a415042674e5648524d4241663845425441444151482f0d0a4d416f4743437147534d343942414d43413067414d45554349474b772b784259364f656b334b6c675957693050346459525a57632b67537343616835513554620d0a4a575959416945413538316b475337347335694a58475950514351416d777531524b4577426139432b625552526e4569676b633d0d0a2d2d2d2d2d454e442043455254494649434154452d2d2d2d2d0d0a",
        "tls_client_certificate": "2d2d2d2d2d424547494e2043455254494649434154452d2d2d2d2d0d0a4d49494252544342374b41444167454341676b416a707851696b2f6852626b77436759494b6f5a497a6a304541774977466a45554d424947413155454177774c0d0a5932787549464a7662335167513045774942634e4e7a55774d5441784d4441774d444177576867504e4441354e6a41784d4445774d4441774d4442614d426f780d0a4744415742674e5642414d4d44324e736269426e636e426a49454e73615756756444425a4d424d4742797147534d34394167454743437147534d3439417745480d0a413049414247516a7057383170623545486749616878497165424e4d4138762f367070515761354f57366b33646e55484f434f465539686e72755630664d4a490d0a367444487363614a6c64327978666970575277712f2b6d32537a4f6a485441624d426b4741315564455151534d42434341324e73626f494a6247396a5957786f0d0a62334e304d416f4743437147534d343942414d43413067414d4555434951446e703555734f64457335304a6e3839596a5367456572635a4952314e70726831610d0a384e6b657736566d32514967523433303231333450654337617477363046524d3338414974433767672f686c78534c304f577a787833673d0d0a2d2d2d2d2d454e442043455254494649434154452d2d2d2d2d0d0a",
        "tls_client_key": "2d2d2d2d2d424547494e2050524956415445204b45592d2d2d2d2d0d0a4d494748416745414d424d4742797147534d34394167454743437147534d3439417745484247307761774942415151676c5a43666461766d53776b4939526c6a0d0a427062636e6f737757355351764348474b7346637744767642794b6852414e434141526b493656764e61572b52423443476f63534b6e67545441504c2f2b71610d0a55466d75546c75704e335a31427a676a685650595a36376c64487a43534f725178374847695a58647373583471566b634b762f70746b737a0d0a2d2d2d2d2d454e442050524956415445204b45592d2d2d2d2d0d0a",
    })

    cln_grpc = una.Node("ClnGrpc", config_cln_grpc)
    print(await cln_grpc.get_info())
    print(await cln_grpc.create_invoice(invoice))
    print(await cln_grpc.pay_invoice(dict({
        "payment_request": "lnbcrt10u1p306998pp53jzmkeummuu0u6rfxpcgx7rk5adturte8mppr64032nek3jmjtvqdq4w3jhxapqvf5kuerfdenhxcqzpgxqrrsssp53nhngg8858l2ch63ks3yc2uetzf4gnctp9xccqxuchztxmahd2as9qyyssqzl6m9rwgwp0r5a6de7fj98k42sn7vvf30n6k2ymcq7wvmk4689ls7zewqq9x5maqa60tshdmhu3gx3dd243vh9h9xralrfrjpfwfn3gq6xml7k"
    })))

async def eclair_rest():
    config_eclair_rest = dict({
        "url": "http://127.0.0.1:8283",
        "username": "",
        "password": "eclairpw"
    })

    eclair_rest = una.Node("EclairRest", config_eclair_rest)
    print(await eclair_rest.get_info())
    print(await eclair_rest.create_invoice(invoice))
    print(await eclair_rest.pay_invoice(dict({
        "payment_request": "lnbcrt10u1p30afdnsp5y05vz3g860fn8fy6fy2u9pr49ttnl6qq85v3mkmzz58cyqxmdpvspp52vy739gahycksqafupk4fw7mu0xjyf2l2e5exr64ycmjedzs3a5sdq4w3jhxapqvf5kuerfdenhxxqyjw5qcqp2rzjq25z6j80gkd8vyr5nptma4lnmhjvyq66eretzvy5a4gty72g8xpejqqqdsqqqqgqqyqqqqlgqqqqqqgq9q9qyysgqp0kpcx20yq5hftwguxfp0aka297g7kqplfl9ntc3rznkwnm9kf94ssq3qygjt2v0jrm95w2s590gc087vr6k3r9fvg9ey58et0dlcdcp978dh6"
    })))

# asyncio.run(lnd_rest())
asyncio.run(cln_grpc())
# asyncio.run(eclair_rest())