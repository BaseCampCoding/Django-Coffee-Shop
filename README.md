# Django Coffee Shop

In this assignment you have been given a mostly complete Django Project.
The frontend for the application has been provided for you.
The only thing missing is:

- the Models
- the URLs
- the Views

More specifically...

## Models

This project represents a coffee store database and has 2 models:

- `Coffee`
- `Transaction`

### `Coffee`

`Coffee` has two fields: `name` and an `price`.

### `Transaction`

`Transaction` has four fields:

- `time`: DateTime of the transaction
- `item` - the coffee purchased
- `pre_tax` - the price of the coffee purchased
- `tax` - tax charged on the purchase (7% of price)

## URLs

- `""` should take you to a view named `"home"`
- `"coffee/<id>/buy"` should take you to a view named `"buy_coffee"`
- `"transaction/<id>"` should take you to a view named `"transaction_detail"`

## Views

- The `home` view should render `"app/coffee_list.html"` and provide
  all `Coffee`s to the context using the key `"coffees"`
- The `transaction_detail` view should use the id provided through the path
  to get the appropriate `Transaction` from the database and render the
  `"app/transaction_detail.html"` template with that `Transaction` provided in the
  context using the key `transaction`
- The `buy_coffee` view should (on POST) create a new `Transaction` in the database
  using the coffee identified in the path.
  It should redirect to `transaction_detail` for the newly created `Transaction`.
