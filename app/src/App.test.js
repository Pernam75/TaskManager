import { render, screen } from '@testing-library/react';
import App from './App';

test('renders task manager button', () => {
  render(<App />);
  const linkElement = screen.getByText(/Task Manager/i);
  expect(linkElement).toBeInTheDocument();
});

test('renders create user button', () => {
  render(<App />);
  const linkElement = screen.getByText(/Create User/i);
  expect(linkElement).toBeInTheDocument();
});

test('renders tasks done card', () => {
  render(<App />);
  const linkElement = screen.getByText(/Tasks Done/i);
  expect(linkElement).toBeInTheDocument();
});

test('renders tasks to do card', () => {
  render(<App />);
  const linkElement = screen.getByText(/Tasks To do/i);
  expect(linkElement).toBeInTheDocument();
});

test('renders add task button', () => {
  render(<App />);
  const linkElement = screen.getByText(/hard/i);
  expect(linkElement).toBeInTheDocument();
});

test('renders users list', () => {
  render(<App />);
  const linkElement = screen.getByText(/Users/i);
  expect(linkElement).toBeInTheDocument();
});

test('renders Github link', () => {
  render(<App />);
  const linkElement = screen.getByText(/Github/i);
  expect(linkElement).toBeInTheDocument();
});

test('renders branch networks button', () => {
  render(<App />);
  const linkElement = screen.getByText(/Branch Networks/i);
  expect(linkElement).toBeInTheDocument();
});

test('renders select user button', () => {
  render(<App />);
  const linkElement = screen.getByText(/ALL/i);
  expect(linkElement).toBeInTheDocument();
});

test('renders quotes', () => {
  render(<App />);
  const linkElement = screen.getByText(/Its not that hard/i);
  expect(linkElement).toBeInTheDocument();
});
